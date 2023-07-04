from django.contrib import admin
from .models import register
from .models import appointment
from .models import login
from .models import adminregister
from .models import adminlogin
from .models import department
from .models import doctors
from .models import addblood
from .models import token
from .models import message
from .models import replays
from .models import labdepartment
from .models import labtest
from .models import report
# Register your models here.
admin.site.register(register)
admin.site.register(appointment)
admin.site.register(login)
admin.site.register(adminregister)
admin.site.register(adminlogin)
admin.site.register(department)
admin.site.register(doctors)
admin.site.register(addblood)
admin.site.register(token)
admin.site.register(message)
admin.site.register(replays)
admin.site.register(labdepartment)
admin.site.register(labtest)
admin.site.register(report)