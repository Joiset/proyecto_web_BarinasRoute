from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Configuración de la visualización del modelo Profile en el Django Admin.
    """
    list_display = ('user', 'role', 'telefono', 'comunidad_sector', 'get_groups')
    list_filter = ('role', 'user__groups')
    search_fields = ('user__username', 'user__email', 'telefono', 'comunidad_sector')

    def get_groups(self, obj):
        return ", ".join([g.name for g in obj.user.groups.all()])
    get_groups.short_description = 'Grupos de Django'