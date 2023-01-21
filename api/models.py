from django.db import models

class Survivor(models.Model):
    ITEMS = ["water", "food", "medication", "ammunition"]

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    infected = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    medication = models.IntegerField(default=0)
    ammunition = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.points = self.calculate_points(self.water, self.food, self.medication, self.ammunition)
        super().save(*args, **kwargs)

    @classmethod
    def calculate_points(cls, water, food, medication, ammunition):
        return (water*4) + (food*3) + (medication * 2) + ammunition