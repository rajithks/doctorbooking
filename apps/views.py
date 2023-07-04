from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import date,timedelta,datetime
from django.contrib import messages
# Create your views here.
def display(request):
    # if 'id' in request.session:
    #     nam = request.session['id']
    #     data = login.objects.get(name=nam)
    return render(request,'index.html')
    # else:
    #     return render(request,'index.html')
def display1(request):
    if 'id' in request.session:
        nam =request.session['id']
        data1 = register.objects.filter(name=nam)
        data = department.objects.all()
        return render(request, 'appointment.html',{'s':data,'name':nam})
    else:
        return render(request,'indexdoctor.html')
def display2(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = register.objects.filter(name=nam)
        return render(request,'contact.html',{'r':data,'name':nam})
    else:
        return render(request,'contact.html')
def display3(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = register.objects.filter(name=nam)
        return render(request,'services.html',{'r':data,'name':nam})
    else:
        return render(request,'services.html')
def display4(request):
    nam = request.GET.get('name')
    data = addblood.objects.all()
    try:
        data1 = addblood.objects.get(name=nam)
        return render(request,'bloodbank.html',{'s':data,'r':data1})
    except(Exception):
        return render(request, 'bloodbank.html', {'s': data})

    # else:
    #     return render(request, 'bloodbank.html')
def display5(request):
    return render(request,'token.html')
def serviceslab(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = report.objects.filter(name=nam)
        data1 = labdepartment.objects.all()
        return render(request,'serviceslab.html',{'s':data1,'name':nam})
    else:
        return render(request, 'indexlab.html')
    #     data1 = register.objects.filter(name=nam)
    #     data = labdepartment.objects.all()
    #     return render(request,'serviceslab.html',{'s':data,'name':data1})
    # else:
    #     return render(request,'indexlab.html')
def indexlab(request):
    if 'id' in request.session:
        id = request.session['id']
        data = register.objects.filter(name=id)
        return render(request,'indexlab.html',{'name':data})
    else:
        return render(request,'indexlab.html')

#user side
def regdis(request):
    return render(request,'registretion.html')
def reg(request):
    if request.method == 'POST':
        nam = request.POST['n1']
        ag = int(request.POST['n2'])
        ph = request.POST['n3']
        gend = request.POST['n4']
        adrs = request.POST['n5']
        pswd = request.POST['n6']
        a = nam
        b = ph
        c = a[:3:1]
        d = b[:3:1]
        e = c+d
        op = e
        data = register.objects.create(name=nam,age=ag,phone=ph,gender=gend,adress=adrs,password=pswd,opnum=op)
        data.save()
        messages.info(request,'data saved')
        return render(request,'registretion.html')
    else:
        return render(request,'registretion.html')
def opdis(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = register.objects.filter(name=nam)
        return render(request, "indexop.html", {'s': data})
    else:
        return render(request,'indexop.html')

def userwelcome(request):
    return render(request,'indexlogin.html')

def doctor(r):
    return render(r,'indexdoctor.html')

def log(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        pswd = int(request.POST['a2'])
        try:
            data = register.objects.get(name=nam)
            if data.password == pswd:
                request.session['id'] = nam
                return redirect(profile)
            else:
                messages.info(request,'incorrect password')
                return render(request,'indexlogin.html')
        except(Exception):
            messages.info(request, 'incorrect name')
            return render(request, 'indexlogin.html')
    else:
        return render(request,'indexlogin.html')

def profile(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = register.objects.filter(name=nam)
        return render(request,'index.html',{'r':data,'name':nam})
    else:
        return redirect(log)
def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(log)

def neurob(request):
    dep = request.GET.get('dep')
    if dep:
        data = doctors.objects.filter(department__name=dep)
        return render(request, 'indexdoctor.html', {'s': data})
    else:
        return render(request,'appointment.html')
def neuroap(request):
    nam = request.GET.get('app')
    l =[]
    if nam:
        data = doctors.objects.filter(name=nam)
        # for i in range(1):
        data1 = datetime.strftime(date.today() + timedelta(days=1),'%Y-%m-%d')
            # print(data1)
        l.append(data1)
        return render(request,'indexappoint.html',{'m':l , 's':data})
    else:
        return render(request, 'appointment.html')
    # if 'id' in request.session:
    #     nam = request.session['id']
    #     data = doctors.objects.all()
    #     return render(request,'indexappoint.html',{'s':data})
def neuroapt(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        op = request.POST['a2']
        ph = int(request.POST['a3'])
        dat = request.POST['a4']
        tim = request.POST['a5']
        depat = request.POST['a6']
        doct = request.POST['a7']
        data = appointment.objects.create(name=nam,opnumber=op,phone=ph,date=dat,time=tim,department=depat,doctor=doct)
        data.save()
        upd = doctors.objects.get(name=doct)
        updated=upd.limit-1
        doctors.objects.filter(name=doct).update(limit=updated)
        try:
            data1 = register.objects.get(opnum=op)
            if data1.name == nam:
                messages.info(request,'Appointment is sended')
                return render(request,'indexappoint.html')
            else:
                messages.info(request, 'incorrect name')
                return render(request, 'indexappoint.html')
        except(Exception):
            messages.info(request, 'incorrect op number')
            return render(request, 'indexappoint.html')
    else:
        return render(request,'index.html')
def tocken(request):
    if request.method == 'POST':
        n = request.POST['a6']
        data = appointment.objects.filter(opnum=n)
        return render(request, 'appointment.html',{'s':data})
    else:
        return render(request,'index.html')
def appoints2(request):
    nam = request.GET.get('name')
    data = appointment.objects.filter(name=nam)
    return render(request,'previousappointments.html',{'s':data})
def appoints(request):
    data = appointment.objects.all()
    return render(request,'displayappoint.html',{'s':data})
def appoints1(request):
    id = request.GET.get('id')
    data = appointment.objects.get(id=id)
    data.status=True
    data.save()
    data1 = appointment.objects.filter(id=id)
    return render(request, 'tokenadmin.html', {'s': data1})
    # return redirect(appoints)


def tokenuser(request):
    data = token.objects.all()
    return render(request,'inbox.html',{'r':data})

def viwblood(request):
    nam = request.GET.get('name')
    try:
        data = addblood.objects.get(name=nam)
        if data is None:
            return render(request, 'addblood.html')
        else:
            messages.info(request, 'you are already registered')
            return render(request, 'bloodbank.html')
    except(Exception):
        return render(request, 'addblood.html')






    # if 'id' in request.session:
    #     nam = request.session['id']
    #     try:
    #         data = addblood.objects.get(name=nam)
    #         if data.name == nam:
    #             messages.info(request, 'you are already registered')
    #             return render(request, 'bloodbank.html')
    #         else:
    #             return render(request, 'addblood.html', {'s': data})
    #     except(Exception):
    #         messages.info(request, 'you are already registered')
    #         return render(request, 'bloodbank.html')




def addetls(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        blood = request.POST['a2']
        ag = request.POST['a3']
        ad = request.POST['a4']
        ph = request.POST['a5']
        data = addblood.objects.create(name=nam,bloodgroup=blood,age=ag,address=ad,phonenumber=ph)
        data.save()
        messages.info(request,'successfully added')
        return render(request,'addblood.html')
    else:
        return render(request,'addblood.html')
def messag(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        ph = request.POST['a2']
        msg = request.POST['a3']
        data = message.objects.create(name=nam,phone=ph,message=msg)
        data.save()
        return redirect(display2)
    else:
        return render(request,'contact.html')
def Laboratory(request):
    if 'id' in request.session:
        nam = request.session['id']
        data = report.objects.filter(name=nam)
        return render(request, 'indexlab.html', {'name': nam})
    else:
        return render(request, 'indexlab.html')
def HAEMATOLOGY(request):
    dep = request.GET.get('LABDEP')
    if dep:
        data = labtest.objects.filter(department__name=dep)
        return render(request,'haematology.html',{'s':data})
    else:
        return render(request,'serviceslab.html')
def newreport(request):
    nam = request.GET.get('name')
    data = report.objects.filter(name=nam)
    return render(request,'report.html',{'s':data})

def history(request):
    return render(request,'reporthis.html')
def emergency(request):
    return render(request,'indexcare.html')
def dischange(request):
    return render(request,'change.html')
def change(request):
    if request.method=='POST':
        nam = request.POST['a1']
        pswd = request.POST['a2']
        register.objects.filter(name=nam).update(password=pswd)
        messages.info(request,'CHANGED')
        return render(request,'change.html')
    else:
        return render(request,'indexlogin.html')
def Therapist(request):
    return render(request,'therapist.html')
#admin side

def admindis(request):
    return render(request,'adminregistration.html')
def adminreg(request):
    if request.method == 'POST':
        nam = request.POST['n1']
        ph = request.POST['n2']
        adrs = request.POST['n3']
        pswd = int(request.POST['n4'])
        data = adminregister.objects.create(name=nam,phone=ph,adress=adrs,password=pswd)
        data.save()
        return HttpResponse("data saved")
    else:
        return render(request,'adminregistration.html')

def adminwelcome(request):
    return render(request,'loginadmin.html')
def adminlog(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        pswd = int(request.POST['a2'])
        try:
            data = adminregister.objects.get(name=nam)
            if data.password == pswd:
                return render(request,'indexadmin.html')
            else:
                messages.info(request,'incorrect password')
                return render(request,'loginadmin.html')
        except(Exception):
            messages.info(request,'incorrect name')
            return render(request,'loginadmin.html')
    else:
        return render(request, 'loginadmin.html')

def admin(request):
    return render(request,'indexadmin.html')

def disdepat(r):
    return render(r,'indexdep.html')
def departments(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        data = department.objects.create(name=nam)
        data.save()
        request.session['id']=nam
        return redirect(disdepat)
    else:
        return render(request,'creatdepat.html')

def disdoct(r):
    return render(r,'creatdoctr.html')
def doctorr(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        educat = request.POST['a2']
        datim = request.POST['a3']
        wek = request.POST['a4']
        depat = request.POST['a5']
        img = request.FILES['a6']
        try:
            data = department.objects.get(name=depat)
            data1=data.id
            data = doctors.objects.create(name=nam,education=educat,datetime=datim,week=wek,department_id=data1,image=img)
            messages.info(request, 'data saved')
            return render(request,'creatdoctr.html')
        except(Exception):
            messages.info(request, 'no such departments')
            return render(request, 'creatdoctr.html')

    else:
        return render(request,'creatdoctr.html')




def disdoctor(request):
    data = doctors.objects.all()
    return render(request,'admindoctor.html',{'s':data})
def upddis(request):
    id = request.GET.get('id')
    data = doctors.objects.filter(id=id)
    # return render(request, 'creatdoctr.html', {'s': data})
    return render(request,'update.html',{'s': data})
def updatedoctor(request):
    id = request.GET.get('name')
    if request.method == 'POST':
        nam = request.POST['a1']
        edu = request.POST['a2']
        datim = request.POST['a3']
        wek = request.POST['a5']
        depat = request.POST['a4']
        data = department.objects.get(name=depat)
        data1 = data.id
        data = doctors.objects.filter(id=id).update(name=nam,education=edu,datetime=datim,week=wek,department_id=data1)
        messages.info(request,'updated')
        return render(request,'update.html')
    else:
        return render(request,'admindoctor.html')
def deletedoctor(request):
    id = request.GET.get('id')
    data = doctors.objects.get(id=id)
    data.delete()
    return redirect(disdoctor)

def disbloodadmin(request):
    data= addblood.objects.all()
    return render(request,'bloodadmin.html',{'s':data})
def add(request):
    id = request.GET.get('id')
    data1 = addblood.objects.get(id=id)
    data1.status=True
    data1.save()
    return redirect(disbloodadmin)
def delete(request):
    id=request.GET.get('id')
    data2 = addblood.objects.filter(id=id)
    data2.delete()
    return redirect(disbloodadmin)
def tokennum(request):
    if request.method=='POST':
        num = request.POST['a1']
        doc = request.POST['a2']
        dep = request.POST['a3']
        pat = request.POST['a4']
        data = token.objects.create(date=num,doctor=doc,department=dep,patient=pat)
        data.status = True
        data.save()
        return redirect(appoints)
    else:
        return render(request,'indexadmin.html')

def complaint(request):
    data = message.objects.all()
    return render(request,'complaint.html',{'s':data})
def disreplay(request):
    id = request.GET.get('id')
    data = message.objects.filter(id=id)
    data.status=True
    return render(request,'replay.html')
def replay(request):
    if request.method=='POST':
        rep = request.POST['a1']
        nam = request.POST['a2']
        name = register.objects.get(name=nam)
        data = replays.objects.create(replay=rep,name=name)
        data.status=False
        data.save()
        messages.info(request,'replay sended')
        return render(request,'replay.html')
    else:
        return render(request,'indexadmin.html')
def inbox(request):
    nam = request.GET.get('name')
    if nam:
        data = replays.objects.filter(name__name=nam)
        data1 = token.objects.filter(patient=nam)
        return render(request,'inbox.html',{'s':data,'name':nam,'r':data1})
    else:
        return render(request,'index.html')
def dislabdepartment(request):
    return render(request, 'labdepartment.html')
def addlabdepartment(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        data = labdepartment.objects.create(name=nam)
        data.save()
        messages.info(request,'data added')
        return render(request,'labdepartment.html')
    else:
        return render(request,'labdepartment.html')

def dislabtests(request):
    return render(request,'labtests.html')
def addlabtest(request):
    if request.method == 'POST':
        nam = request.POST['a1']
        amount = request.POST['a2']
        depat = request.POST['a3']
        try:
            data = labdepartment.objects.get(name=depat)
            data1 = data.id
            data = labtest.objects.create(name=nam,price=amount,department_id=data1)
            data.save()
            messages.info(request, 'DATA SAVED')
            return render(request, 'labtests.html')
        except(Exception):
            messages.info(request, 'no such tables')
            return render(request, 'labtests.html')

    else:
        return render(request,'labtests.html')
def disreport(request):
    return render(request, 'adminreport.html')
def repot(request):
    if request.method == 'POST':
        nam = request.POST['a2']
        img = request.FILES['a1']
        data = report.objects.create(name=nam,image=img)
        data.save()
        messages.info(request,'DATA SENDED')
        return render(request, 'adminreport.html')
    else:
        return render(request,'adminreport.html')
def cancel(request):
    id = request.GET.get('id')
    data = appointment.objects.filter(id=id)
    data.delete()
    return redirect(appoints2)
def disreg(request):
    data = register.objects.all()
    return render(request,'disreg.html',{'s':data})
def disdep(request):
    data = department.objects.all()
    return render(request,'disdep.html',{'s':data})
def dislabdep(request):
    data = labdepartment.objects.all()
    return render(request,'dislabdep.html',{'s':data})
def labdepdel(request):
    id = request.GET.get('id')
    data = labdepartment.objects.filter(id=id)
    data.delete()
    return redirect(dislabdep)
    # messages.info(request,'deleted')
    # return render(request,'dislabdep.html')
def depdel(request):
    id = request.GET.get('id')
    data = department.objects.filter(id=id)
    data.delete()
    return redirect(disdep)
    # messages.info(request, 'deleted')
    # return render(request, 'disdep.html')
def appointdel(request):
    id = request.GET.get('id')
    data = appointment.objects.filter(id=id)
    data.delete()
    return redirect(appoints)
def available(request):
    id = request.GET.get('id')
    data = doctors.objects.get(id=id)
    data.status = False
    data.save()
    return redirect(disdoctor)
def leave(request):
    id =request.GET.get('id')
    data = doctors.objects.get(id=id)
    data.status = True
    data.save()
    return redirect(disdoctor)
def reset(request):
    id = request.GET.get('id')
    data = doctors.objects.get(id=id)
    data.limit=10
    data.save()
    return redirect(disdoctor)
def search(request):
    if request.method=='POST':
        op = request.POST['a1']
        try:
            data = appointment.objects.filter(opnumber=op)
            return render(request,'search.html',{'s':data})
        except(Exception):
            messages.info(request,'This op number not exist')
            return render(request,'search.html')
    else:
        return render(request,'disreg.html')
