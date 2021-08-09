from django.test import TestCase
from .models import USWDML


class PostTestCase(TestCase):
    def test_post(self):
        self.assertEquals(USWDML.objects.count(),0)
        wdml_data = {
                 'case_id' : 37,
                 't_state' : 'TX',
                 'p_name' : 'Test_Project',
                 'p_year' : 1992,
                 'p_tnum' : 27,
                 'p_cap' : '4.5',
                 't_manu' : 'Stark',
                 't_model' : 'Best',
                 't_cap' : '2.3',
                 't_hh' : '3.7',
                 'x_long' : 18.234,
                 'y_lat' : -12.23,
             }
        USWDML.objects.create(**wdml_data)
        self.assertEquals(
            USWDML.objects.count(),
            1
        )

# Create your tests here.
