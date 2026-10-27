from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Extensión del usuario estándar de Django para gestionar los roles del sistema BarinasRoute.
    """
    ROLE_CHOICES = (
        ('administrador', 'Administrador'),
        ('gestor', 'Gestor de Transporte'),
        ('usuario', 'Usuario / Ciudadano'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Usuario")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='usuario', verbose_name="Rol asignado")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    comunidad_sector = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sector o Urbanización")

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"