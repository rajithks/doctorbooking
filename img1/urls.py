"""img1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.profile),
    path('register.html',views.reg),
    path('register',views.reg),
    path('login.html',views.log),
    path('index.html',views.profile),
    path('appointment.html',views.display1),
    path('contact.html',views.display2),
    path('services.html',views.display3),
    path('bloodbank.html',views.display4),
    path('token.html',views.display5),
    path('1',views.doctor),
    path('neurology',views.neurob),
    path('appointment',views.neuroap),
    path('appointments',views.neuroapt),
    path('2att',views.tocken),
    # path('3',views.casual),
    # path('dentistry',views.dental),
    # path('cardiology',views.cardi),
    # path('orthopedic',views.ortho),
    # path('pediatrics',views.pediat),
    # path('Ent',views.ent),
    # path('gynecology',views.gyne),
    # path('physician',views.physi),
    path('11',views.admin),
    path('adminpage',views.adminwelcome),
    path('userpage',views.userwelcome),
    path('userreg',views.regdis),
    path('login',views.log),
    path('13',views.logout),
    path('admindisplay',views.admindis),
    path('adminlogin',views.adminlog),
    path('adminreg',views.adminreg),
    path('department',views.departments),
    path('16',views.doctorr),
    path('adddepartment',views.disdepat),
    path('doc',views.disdoct),
    path('doctor',views.disdoctor),
    path('op',views.opdis),
    path('viwblood',views.viwblood),
    path('blood',views.addetls),
    path('19',views.add),
    path('20',views.delete),
    path('bloodadmin',views.disbloodadmin),
    path('update',views.upddis),
    path('update1',views.updatedoctor),
    path('delete',views.deletedoctor),
    path('appoints',views.appoints),
    path('appoints2',views.appoints2),
    path('appoints1',views.appoints1),
    path('token',views.tokennum),
    path('viewtoken',views.tokenuser),
    path('message',views.messag),
    path('complaint',views.complaint),
    path('replay.html',views.disreplay),
    path('replay',views.replay),
    path('inbox',views.inbox),
    path('Laboratory',views.Laboratory),
    path('serviceslab.html',views.serviceslab),
    path('indexlab.html',views.indexlab),
    path('labdepartment',views.dislabdepartment),
    path('labtests',views.dislabtests),
    path('addlabdepartment',views.addlabdepartment),
    path('addlabtest',views.addlabtest),
    path('HAEMATOLOGY',views.HAEMATOLOGY),
    # path('BIOCHEMISTRY',views.BIOCHEMISTRY),
    # path('BLOOD',views.BLOOD),
    # path('DRUG',views.DRUG),
    # path('URINE',views.URINE),
    # path('FLUID',views.FLUID),
    path('newreport',views.newreport),
    path('history',views.history),
    path('report',views.disreport),
    path('sendreport',views.repot),
    path('emergency',views.emergency),
    path('change',views.dischange),
    path('changed',views.change),
    path('cancel',views.cancel),
    path('Therapist',views.Therapist),
    path('disreg',views.disreg),
    path('disdep',views.disdep),
    path('dislabdep',views.dislabdep),
    path('depdel',views.depdel),
    path('labdepdel',views.labdepdel),
    path('appointdel',views.appointdel),
    path('available',views.available),
    path('leave',views.leave),
    path('reset',views.reset),
    path('search',views.search)

    # path('chatsend',views.chat)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
