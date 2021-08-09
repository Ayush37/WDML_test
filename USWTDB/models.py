from django.db import models

# Create your models here.
class USWDML(models.Model):
    case_id = models.IntegerField()
    t_state = models.CharField(max_length=255)
    p_name = models.TextField()
    p_year = models.IntegerField()
    p_tnum = models.IntegerField()
    p_cap = models.CharField(max_length=255)
    t_manu = models.TextField()
    t_model = models.TextField(null=True)
    t_cap = models.CharField(max_length=255)
    t_hh = models.CharField(max_length=255,null=True)
    x_long = models.CharField(max_length=255)
    y_lat = models.CharField(max_length=255)
