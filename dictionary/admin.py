from django.contrib import admin
from dictionary.models import GeoLocationType, Dictionary, Word

class GeoLocationTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(GeoLocationType, GeoLocationTypeAdmin)

class WordInline(admin.StackedInline):
    model = Word

class DictionaryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Types', {
            'classes': ('collapse',),
            'fields': ('types',)
        })
    )

    inlines = [
        WordInline,
    ]
    

admin.site.register(Dictionary, DictionaryAdmin)