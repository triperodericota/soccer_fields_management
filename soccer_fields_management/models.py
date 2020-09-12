from django.db import models
from django.utils import timezone

# Create your models here.

class SoccerField(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    locker_room = models.BooleanField('Locker room')
    ilumination = models.BooleanField()
    syntehtic_grass =models.BooleanField('Synthetic Grass')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['code']

class Rental(models.Model):
    client = models.CharField(max_length=50)
    employee = models.CharField(max_length=50, help_text='How did take the rental?')
    rental_date = models.DateField('Date', default=timezone.now())
    turn = models.DateTimeField('Date and Time Turn', help_text='When is the match going to play?')
    soccer_field = models.ForeignKey(SoccerField, on_delete=models.CASCADE)

    def has_got_for(self):
        return Rental.objects.filter(soccer_field=self.soccer_field).filter(turn=self.turn).exists()

    def has_got_for_update(self):
        return Rental.objects.filter(soccer_field=self.soccer_field).filter(turn=self.turn).exclude(pk__in=[self.pk]).exists()

    class Meta:
        ordering = ['-turn']
        get_latest_by = 'rental_date'