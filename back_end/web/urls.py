from django.urls import path

from web import views, api

urlpatterns = [
    path('', views.index, name='web/index'),

    path('cadastrar', views.register, name='web/register'),
    path('capturar', views.capture, name='web/capture'),
    path('atualizar-horarios', views.update_shifts, name='web/update-shifts'),
    path('baixar-frequencia', views.export, name='web/export'),
    path('treinar', views.train, name='web/train'),

    path('api/ping', api.ping),
    path('api/recognition', api.recognition),
    path('api/register', api.register)
]
