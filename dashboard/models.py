from django.db import models
from PIL import Image

class PhoneBrands(models.Model):
    BrandName= models.CharField(max_length=300,default='null')
    BrandLogo = models.ImageField(upload_to='brand_logo')

    def __str__(self):
        return f'{self.BrandName}'

class PhoneModels(models.Model):
    brand = models.ForeignKey(PhoneBrands,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=300 )
    model_variant = models.CharField(max_length=300)
    model_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    model_img = models.ImageField(upload_to='model_img')

    def __str__(self):
        return f'{self.model_name,self.brand}'

    def save(self):
        super().save()

        img = Image.open(self.model_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.model_img.path)




