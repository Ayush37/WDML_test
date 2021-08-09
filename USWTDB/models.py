from django.db import models

# Create your models here.
class USWDML(models.Model):
    case_id = models.IntegerField(null=True)
    t_state = models.CharField(max_length=255,null=True)
    p_name = models.TextField(null=True)
    p_year = models.IntegerField(null=True,default=0000)
    p_tnum = models.IntegerField(null=True)
    p_cap = models.CharField(max_length=255,null=True)
    t_manu = models.TextField(null=True)
    t_model = models.TextField(null=True)
    t_cap = models.CharField(max_length=255,null=True)
    t_hh = models.CharField(max_length=255,null=True)
    x_long = models.CharField(max_length=255,null=True)
    y_lat = models.CharField(max_length=255,null=True)
