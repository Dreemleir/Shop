from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(validators=[MinValueValidator(0)])

    SIZES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )

    size = MultiSelectField(choices=SIZES)
    currency = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{0}".format(self.name)

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])