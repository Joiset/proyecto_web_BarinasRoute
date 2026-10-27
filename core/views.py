from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Vista principal de BarinasRoute.
    Muestra la información según el rol:
    - Visitante: catálogo público e información institucional.
    - Usuario: rutas activas y accesos directos para reportar.
    - Gestor: panel de moderación de avisos y unidades.
    - Administrador: enlaces de control general del sistema.
    """
    return render(request, 'core/home.html')

@login_required
def dashboard_view(request):
    """
    Panel privado que se adapta al rol autenticado.
    """
    rol = getattr(request.user.profile, 'role', 'usuario')
    contexto = {
        'rol': rol
    }
    return render(request, 'core/dashboard.html', contexto)