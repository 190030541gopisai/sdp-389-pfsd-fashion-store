from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    p_type_choices=(
        ('Men','Men'),
        ('Women','Women'),
        ('Kids','kids')
    )
    p_category_choices = (
        ('men', (
                    ('Sherwani','Sherwani'),
                    ('Tshirts','Tshirts'),
                    ('Formals','Formals')
                )
        ),
        ('women', (
                    ('Kurtis','Kurtis'),
                    ('Sarees','Sarees'),
                    ('Lehangachouli','Lehangachouli')
                )
        ),
        ('kid', (
                    ('Traditional','Traditional'),
                    ('Tshirts','Tshirts'),
                    ('OneSies','OneSies')
                )
        )
    )

    p_name = models.CharField(max_length=30,unique = True)
    p_image = models.ImageField(default='productpics/default.png',upload_to='productpics')
    p_type = models.CharField(
        max_length=100,
        choices = p_type_choices
    )
    p_category = models.CharField(
        max_length=100,
        choices = p_category_choices
    )
    p_cost = models.DecimalField(max_digits=6,decimal_places=2)
    p_description = models.TextField()
    
    def get_absolute_url(self):
        return reverse('sherwani',kwargs={'sherwani':self.p_category})


    def __str__(self):
        return f'Product {self.id} {self.p_type}-{self.p_name}-{self.p_category}'