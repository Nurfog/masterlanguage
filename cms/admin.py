from django.contrib import admin
import cms.models as models

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    search_fields = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    list_filter = ('id', 'rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razonsocial')
    readonly_fields = ('id',)

admin.site.register(models.empresa, EmpresaAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    search_fields = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    list_filter = ('id', 'empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'empresa')
    readonly_fields = ('id',)

admin.site.register(models.representante, RepresentanteAdmin)

class paisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(models.pais, paisesAdmin)

class regionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'codigo')
    readonly_fields = ('id',)

admin.site.register(models.region, regionesAdmin)

class provinciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'region', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'region', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'region')
    readonly_fields = ('id',)

admin.site.register(models.provincia, provinciasAdmin)

class comunasAdmin(admin.ModelAdmin):
    list_display = ('id', 'provincia', 'codigo', 'nombre', 'estado')
    search_fields = ('id', 'provincia', 'codigo', 'nombre', 'estado')
    list_filter = ('id', 'provincia', 'codigo', 'nombre', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'provincia')
    readonly_fields = ('id',)

admin.site.register(models.comuna, comunasAdmin)

class colegiosAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    search_fields = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    list_filter = ('id', 'razon_social', 'comuna', 'direccion', 'telefono', 'email', 'estado')
    ordering = ['id']
    list_per_page = 10
    list_editable = ('estado',)
    list_display_links = ('id', 'razon_social')
    readonly_fields = ('id',)

admin.site.register(models.colegio, colegiosAdmin)

