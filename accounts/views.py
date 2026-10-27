from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserRegisterForm

def register_view(request):
    """
    Controlador para el registro de nuevos usuarios en BarinasRoute.
    Si el formulario es válido, guarda el usuario e inicia su sesión directamente.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserRegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    """
    Cierra la sesión del usuario actual y lo redirige a la página principal.
    """
    logout(request)
    return redirect('home')