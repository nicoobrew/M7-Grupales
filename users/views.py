from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .forms import SuperRegisterForm, RegistrationForm
from django.contrib.auth.models import Group
from django.views import generic, View
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy

# Create your views here.
def view_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.has_perm('logistica'):
                return redirect('store:orders')
            else:    
                return redirect('store:welcome')
    
    return redirect('store:index')


def public_registration(request):
    return render(request, 'public_registration.html')
    
class PublicRegisterView(generic.edit.FormView):
    template_name = 'users/form_render.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:email_confirmation')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = get_random_string(length=6)
        user.set_password(password)
        user.save()

        # Envía el correo con la contraseña aleatoria
        subject = 'Contraseña de confirmación'
        message = f'Su contraseña de confirmación es: {password}'
        from_email = settings.EMAIL_HOST_USER  
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)

class EmailConfirmationView(View):
    template_name = 'users/email_confirmation.html' 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def superuser_form(request):
    if request.method == "POST":
        form = SuperRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            chosen_rol = form.cleaned_data["type_user"]
            if chosen_rol == "staff":
                rol = Group.objects.get(name="staff")
            elif chosen_rol == "vendedor":
                rol = Group.objects.get(name="vendedor")
            elif chosen_rol == "logistica":
                rol = Group.objects.get(name="logistica")
            user.save()
            user.groups.add(rol)

            return redirect('store:index')

        else:
            messages.error(request, "Error en el registro")
    form = SuperRegisterForm()
    return render(request, 'users/superuser_form.html', {'form':form})
