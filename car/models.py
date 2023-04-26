from django.db import models
# Create your models here.

class Cartype(models.Model):
     name = models.CharField(max_length=100)

     class Meta:
        db_table = 'car type'

     def __str__(self):
        return self.name
     
class Carvarient(models.Model):
     name = models.CharField(max_length=100)

     class Meta:
        db_table = 'car Varient'

     def __str__(self):
        return self.name

class CarEngineandTransmission(models.Model):
    enginetype = models.CharField(max_length=50)
    enginedisplacement = models.IntegerField(null=True)
    noofcylinder = models.IntegerField(null=True)
    maxpower = models.IntegerField(null=True)
    torque = models.IntegerField(null=True)
    transmissiontype = models.CharField(max_length=100)
    drivetype = models.CharField(max_length=50)
    cluchtype = models.CharField(max_length=50)

    class Meta:
        db_table = 'CarEngine and Transmission'

    def __str__(self):
        return self.enginetype


class Fuel(models.Model):
     
      fueltype = models.CharField(max_length=100)
      tankcapicity = models.IntegerField(null=True)
      topspeed = models.IntegerField(null=True)
      mileage = models.IntegerField(null=True)

      class Meta:
          db_table = 'Fuel'

      def __str__(self):
        return self.fueltype

class Exterior(models.Model):
    wheel =  models.IntegerField(null=True)
    colors = models.CharField(max_length=100)

    class Meta:
        db_table = 'exterior'

    def __str__(self):
        return self.colors


class Brand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name

class Comfort(models.Model):
    vanitymirror = models.BooleanField(default=True)
    realseatheadrest = models.BooleanField(default=True)
    adjustableheadrest = models.BooleanField(default=True)
    rearseatcentrearmrest = models.BooleanField(default=True)
    heightadjustablefrontseatbelts = models.BooleanField(default=True)
    rearACVents = models.BooleanField(default=True)
    seatLumbarSupport = models.BooleanField(default=True)
    multifunctionSteeringWheel = models.BooleanField(default=True)
    cruiseControl = models.BooleanField(default=True)

    class Meta:
        db_table = 'comfort'

    def __str__(self):
        return str(self.vanitymirror)



    
class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    exterior = models.ForeignKey(Exterior,on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    carvarient = models.ForeignKey(Carvarient,on_delete=models.CASCADE)
    cartype = models.ForeignKey(Cartype,on_delete=models.CASCADE)
    comfort = models.ForeignKey(Comfort,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/',null=True,blank=True)

    class Meta:
        db_table = 'car'

    def __str__(self):
        return self.name
    