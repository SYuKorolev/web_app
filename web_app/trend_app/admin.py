from django.contrib import admin
from trend_app.models import Description, Trend

class DescAdmin(admin.ModelAdmin):
    pass

class TrendAdmin(admin.ModelAdmin):
    pass

admin.site.register(Description, DescAdmin)
admin.site.register(Trend, TrendAdmin)