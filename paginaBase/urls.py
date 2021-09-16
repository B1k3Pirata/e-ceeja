from django.urls import path
from .views import IndexView

app_name = 'paginas'

urlpatterns = [
    #path('/login',auth_views.LoginView.as_view(
    #    template_name='paginas/allauth/account/form.html'
    #    ), name='login'
    #),
    #path('/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name = 'inicio'),
]
