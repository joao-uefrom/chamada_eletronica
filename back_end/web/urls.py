from django.urls import path

from web import views

urlpatterns = [
    path('', views.index, name='web/index'),

    path('cadastrar', views.register, name='web/register'),
    path('capturar', views.capture, name='web/capture'),
    path('atualizar-horarios', views.update_shifts, name='web/update-shifts'),
    path('baixar-frequencia', views.export, name='web/export'),
    path('treinar', views.train, name='web/train'),

    path('api/ping', controllers.ping),
    path('api/recognition', controllers.recognition),
    path('api/register', controllers.register)
]
