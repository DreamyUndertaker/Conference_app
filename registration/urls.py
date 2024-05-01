from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path

from Conference import settings
from registration.forms import UserLoginForm
from registration.views import RegistrationView, LoginView

urlpatterns = [
    path("signup/", RegistrationView.as_view(template_name='registration/registration.html'),
         name="signup"),
    path('login/', LoginView.as_view(form_class=UserLoginForm, template_name="registration/login.html"),
         name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
