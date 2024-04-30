from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import UserLoginForm, RegistrationForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm  # Ваша форма входа
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home:home')  # Редирект на домашнюю страницу после успешной авторизации


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.role = self.request.POST.get('role')  # Добавляем роль пользователя
        return super().form_valid(form)
