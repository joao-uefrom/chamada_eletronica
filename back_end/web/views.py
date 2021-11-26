from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

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
