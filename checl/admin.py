from django.contrib import admin
from .models import Candidate

class Dis(admin.ModelAdmin):
    list_display = ("name", "ville", "gender", "assertion1", "assertion2", "assertion3", "assertion4",
                    "assertion5", "assertion6", "assertion7", "assertion8", "assertion9")

admin.site.register(Candidate, Dis)