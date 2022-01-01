from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile


class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = UserCreationFormWithEmail
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    # model = Profile
    form_class = ProfileForm
    # fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self, queryset=None):
        # recupera el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    # @method_decorator(login_required, name='dispatch')
# class ProfileUpdate(TemplateView):
#     template_name = 'registration/profile_form.html'


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self, queryset=None):
        # recupera el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form
