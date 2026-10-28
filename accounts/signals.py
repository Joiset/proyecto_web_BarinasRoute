from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile_and_group(sender, instance, created, **kwargs):
    """
    Asigna automáticamente el perfil y el grupo por defecto al registrarse un usuario.
    
    """
    if created:
        # Se crea el perfil asociado en la base de datos
        profile = Profile.objects.create(user=instance)

        # Se asegura la existencia del grupo 'Usuario' y se lo vincula
        grupo_usuario, _ = Group.objects.get_or_create(name='Usuario')
        instance.groups.add(grupo_usuario)

        # Si se crea como superusuario desde consola, se promueve a Administrador
        if instance.is_superuser:
            profile.role = 'administrador'
            grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
            instance.groups.add(grupo_admin)
            profile.save()