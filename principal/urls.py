
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout

urlpatterns = [
    path('', index, name='index'),
    path('teste/', teste, name='teste'),
    path('cadastro_trabalho/', trabalho_novo, name='cadastro_trabalho'),
    path('editar_trabalho/<int:id>/', editar_trabalho, name='editar_trabalho'),
    path('trabalho_list', trabalho_list, name="trabalho_list"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),

]