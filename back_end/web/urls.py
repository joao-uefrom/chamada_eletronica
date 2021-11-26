from django.urls import path

from web import api, forms, views

urlpatterns = [
    path('', views.index, name='web/index'),

    path('cadastrar', forms.register, name='web/register'),
    path('capturar', forms.capture, name='web/capture'),
    path('atualizar-horarios', forms.update_shifts, name='web/update-shifts'),
    path('baixar-frequencia', forms.export, name='web/export'),
    path('treinar', forms.train, name='web/train'),

    path('api/ping', api.ping),
    path('api/recognition', api.recognition),
    path('api/register', api.register)
]
