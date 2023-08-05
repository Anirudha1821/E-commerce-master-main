import uuid
from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name=models.CharField(max_length=60)
    product_desc=models.CharField(max_length=200)
    category=models.CharField(max_length=200,default="")
    subcategory=models.CharField(max_length=200,default="")
    price=models.IntegerField(default=0)
    product_pub_date=models.DateField()
    image=models.ImageField(upload_to="images",default="")
    
    class Meta:
        # we can set manualy values to  set the plural name of the model.
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
    # to add product name to data added row 
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    phoneno=models.CharField(max_length=60,default="")
    email = models.CharField( max_length=50,default="")
    desc=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

    
    
