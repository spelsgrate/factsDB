from django.db import models

# Create your models here.
from django.db import models

class Facts(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    area = models.IntegerField(blank=True, null=True)
    area_land = models.IntegerField(blank=True, null=True)
    area_water = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_growth = models.TextField(blank=True, null=True)  # This field type is a guess.
    birth_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    death_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    migration_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facts'
