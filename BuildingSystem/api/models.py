from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile =models.CharField(max_length=15)
    
    def __str__(self):
        return self.name


    def device(self):
        return Device.objects.filter(room=self)


class Room(models.Model):
    
    number = models.CharField(max_length=10)
    building = models.ForeignKey(Building,related_name='rooms', on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Room '+self.number

class Device(models.Model):

    room = models.ForeignKey(Room, related_name='devices',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    
