import codecs
import csv
from datetime import datetime, time, timedelta
from threading import Thread

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import recognition.core as recognition
from . import utils
from .models import Totem, Student, Shift, Entry, Config


def index(request):
    current_time = datetime.now()

    shifts = Shift.objects.all()
    students = Student.objects.all()
    totens = Totem.objects.all()

    current_shift = ''
    entries = []
    entry_tolerance = Config.objects.get(key='entry_tolerance').value
    shift_students = []

    for shift in shifts:
        if shift.open <= current_time.time() <= shift.close:
            current_shift = shift.name

            start_time = current_time.replace(hour=shift.open.hour, minute=shift.open.minute, second=0)
            end_time = current_time.replace(hour=shift.close.hour, minute=shift.close.minute, second=59)

            shift_students = students.filter(shift=shift)

            entries = Entry.objects.all().filter(created_at__range=(start_time, end_time))
            break

    coverage_model = round(students.filter(training=True).count() * 100 / len(students), 2) if len(students) > 0 else 0
    is_training = bool(Config.objects.get(key='is_training').value)
    ratio = int((len(entries) / len(shift_students)) * 100) if len(shift_students) > 0 else 0

    paginator = Paginator(students, 5)
    page_number = request.GET.get('pagina', 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'web/index.html', {
            'coverage_model': coverage_model,
            'current_shift': current_shift,
            'entries': entries,
            'entry_tolerance': entry_tolerance,
            'is_training': is_training,
            'page_number': page_number,
            'page_obj': page_obj,
            'ratio': ratio,
            'shift_students': shift_students,
            'shifts': shifts,
            'totens': totens
        }
    )


def capture(request: HttpRequest):
    if request.method == 'POST':
        mac_address = request.POST.get('mac_address', default='')
        mac_address = utils.sanitize(mac_address)

        totem = Totem.objects.get(mac_address=mac_address)

        if totem.student:
            totem.student = None
            totem.save()

            messages.success(request, 'Modo de captura encerrado.')
            return redirect('web/index')

        cpf = request.POST.get('cpf', default='')
        cpf = utils.sanitize(cpf)

        try:
            student = Student.objects.get(cpf=cpf)
        except Student.DoesNotExist:
            messages.warning(request, 'CPF não cadastrado.')
            return redirect('web/index')

        totem.student = student
        totem.save()

        messages.success(request, 'Modo de captura iniciado.')

    return redirect('web/index')


def register(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name', default='')
        cpf = request.POST.get('cpf', default='')
        enrolment = request.POST.get('enrolment', default='')
        c_lass = request.POST.get('class', default='')
        shift = request.POST.get('shift', default='')

        if not (name and cpf and enrolment and c_lass and shift):
            messages.warning(request, 'Não deixe campos vazios.')
            return redirect('web/index')

        if not utils.is_valid_cpf(cpf):
            messages.warning(request, 'CPF inválido.')
            return redirect('web/index')

        try:
            Student.objects.create(
                name=name,
                cpf=utils.sanitize(cpf),
                enrolment=enrolment,
                c_lass=c_lass,
                shift_id=shift
            )
        except IntegrityError:
            messages.warning(request, 'Não foi possível cadastrar o aluno.')
            return redirect('web/index')

        messages.success(request, 'Aluno cadastrado com sucesso.')

    return redirect('web/index')


def update_shifts(request: HttpRequest):
    if request.method == 'POST':
        shifts = Shift.objects.all()
        entry_tolerance = Config.objects.get(key='entry_tolerance')

        entry_tolerance.value = int(request.POST.get('entry_tolerance', default='0'))

        for shift in shifts:
            open: str = request.POST.get(f'{shift.id}.open', default='00:00')
            close: str = request.POST.get(f'{shift.id}.close', default='00:00')

            new_open = time(hour=int(open.split(':')[0]), minute=int(open.split(':')[1]))
            new_close = time(hour=int(close.split(':')[0]), minute=int(close.split(':')[1]))

            if new_open > new_close:
                messages.warning(request, 'Não foi possível salvar o horário.')
                return redirect('web/index')

            shift.open = new_open
            shift.close = new_close

        for shift in shifts:
            for shift_j in shifts:
                if shift == shift_j:
                    continue

                if shift_j.open <= (shift.open or shift.close) <= shift_j.close:
                    messages.warning(request, 'Não foi possível salvar o horário.')
                    return redirect('web/index')

        for shift in shifts:
            shift.save()

        entry_tolerance.save()

        messages.success(request, 'Horário atualizado.')

    return redirect('web/index')


def export(request: HttpRequest):
    if request.method == 'POST':
        today = datetime.today()
        default_date = f'{today.day}/{today.month}/{today.year}'

        export_from = request.POST.get('export-from', default=default_date)
        export_to = request.POST.get('export-to', default=default_date)

        start_date = datetime.strptime(export_from, '%d/%m/%Y')
        end_date = datetime.strptime(export_to, '%d/%m/%Y') + timedelta(days=1, seconds=-1)

        if start_date > end_date:
            messages.warning(request, 'Não foi possível exportar os dados.')
            return redirect('web/index')

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="relatorio-de-frequencia.csv"'
        response.write(codecs.BOM_UTF8)

        entries = Entry.objects.all().filter(created_at__range=(start_date, end_date))

        header = [
            'aluno',
            'matricula',
            'data_hora',
            'totem'
        ]

        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()

        for entry in entries:
            writer.writerow(
                {
                    'aluno': entry.student.name,
                    'matricula': entry.student.enrolment,
                    'data_hora': datetime.strftime(entry.created_at, '%d/%m/%Y %H:%M:%S'),
                    'totem': entry.totem.mac_address
                }
            )

        return response

    return redirect('web/index')


def train(request: HttpRequest):
    if request.method == 'POST':
        is_training = Config.objects.get(key='is_training')

        if is_training.value:
            return redirect('web/index')

        is_training.value = 'true'
        is_training.save()

        Thread(target=__training, args=(is_training,)).start()

        messages.success(request, 'Treinamento do modelo iniciado.')

    return redirect('web/index')


def __training(is_training):
    recognition.train()
    students = Student.objects.all().filter(training=False)

    for student in students:
        if student.photos > 0:
            student.training = True
            student.save()

    is_training.value = None
    is_training.save()
