from django.db import models
class register(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    phone = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    adress = models.TextField()
    password = models.IntegerField()
    opnum = models.CharField(max_length=10)
    def __str__(self):
        return self.name
class login(models.Model):
    name = models.CharField(max_length=40)
    password = models.IntegerField()
    def __str__(self):
        return self.name
class adminregister(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    adress = models.TextField()
    password = models.IntegerField()
    def __str__(self):
        return self.name
class adminlogin(models.Model):
    name = models.CharField(max_length=40)
    password = models.IntegerField()
    def __str__(self):
        return self.name

class department(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class doctors(models.Model):
    name = models.CharField(max_length=40)
    education = models.CharField(max_length=150)
    datetime = models.CharField(max_length=100)
    week = models.CharField(max_length=100)
    image = models.FileField()
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    limit = models.IntegerField(default=10)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class appointment(models.Model):
    name = models.CharField(max_length=40)
    opnumber = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    doctor = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class token(models.Model):
    date = models.CharField(max_length=40)
    doctor = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    patient = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.number
class addblood(models.Model):
    name = models.CharField(max_length=40)
    bloodgroup = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class message(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    message = models.TextField()
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class replays(models.Model):
    replay = models.CharField(max_length=100)
    name = models.ForeignKey(register,on_delete=models.CASCADE,blank=True)
    status = models.BooleanField(default=True)

class labdepartment(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class labtest(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    department = models.ForeignKey(labdepartment, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class report(models.Model):
    name = models.CharField(max_length=40)
    image = models.FileField()
    # def __str__(self):
    #     return self.image
# class appointment(models.Model):
#     name = models.CharField(max_length=40)
#     age = models.IntegerField()
#     opnum = models.CharField(max_length=40)
#     phone = models.IntegerField()
#     date = models.DateField(max_length=40)
#     def __str__(self):
#         return self.name


