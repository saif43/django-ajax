from django.contrib import admin
from .models import Divisions, Districts

# Register your models here.



class DistrictAdmin(admin.ModelAdmin):
    list_show = ('name','education_rate','population_density','visited','Divisions')


admin.site.register(Divisions)
admin.site.register(Districts, DistrictAdmin)