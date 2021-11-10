from datetime import datetime, timedelta

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse

from recognition.core import recognition_face, add_face
from . import utils
from .models import Totem, Student, Entry, Config


def ping(request: HttpRequest):
    ip = utils.get_ip(request)
    mac_address = utils.get_mac_address(request)

    if not utils.is_valid_mac_address(mac_address):
        return HttpResponseBadRequest()

    client = Totem.objects.get_or_create(mac_address=mac_address)[0]
    client.ip = ip
    client.save()

    return HttpResponse()


def register(request: HttpRequest):
    image_data = request.read()
    mac_address = utils.get_mac_address(request)

    totem = Totem.objects.get(mac_address=mac_address)
    student = totem.student

    if not student or request.content_type is None:
        return HttpResponse()

    add_face(student.cpf, image_data, request.content_type)

    student.photos += 1
    student.save()

    return HttpResponse()


def recognition(request: HttpRequest):
    image_data = request.read()
    mac_address = utils.get_mac_address(request)

    results = recognition_face(image_data)

    if len(results) != 1:
        return JsonResponse({'erro': 'Nenhum ou mais de um resultado encontrado'}, status=422)

    totem = Totem.objects.get(mac_address=mac_address)
    student = Student.objects.get(cpf=results[0][0])

    __make_entry(totem, student)

    return JsonResponse({
        'class': student.c_lass,
        'enrolment': student.enrolment,
        'name': student.name,
        'shift': student.shift.name
    })


def __make_entry(totem, student):
    current_time = datetime.now()

    entry = Entry.objects.filter(created_at__day=current_time.day, student=student)

    if len(entry) > 0:
        return

    entry_tolerance = int(Config.objects.get(key='entry_tolerance').value)
    shift_open = datetime.combine(current_time.date(), student.shift.open) + timedelta(minutes=entry_tolerance)

    if current_time > shift_open:
        return JsonResponse({'erro': 'Entrada negada, aluno atrasado.'}, status=422)
    else:
        Entry.objects.create(student=student, client=totem)
