from django.contrib import admin



from scrape.models import Filters

@admin.register(Filters)
class AuthorAdmin(admin.ModelAdmin):
    pass


