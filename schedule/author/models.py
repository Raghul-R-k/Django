from django.db import models # type: ignore
from django.core.validators import MinValueValidator,MaxValueValidator # type: ignore
from django.utils.text import slugify 
# Create your models here.
class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(20)])
    city = models.CharField(max_length=100,null=True)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),MinValueValidator(2)
    ],null=True)

    # full_name = models.CharField(max_length=20,null=True)
    slug = models.SlugField(default='',db_index=True,null=True,editable=False)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.first_name+" "+self.last_name)
        # self.slug = slugify(self.full_name)
        super().save(*args,**kwargs)

    def __str__(self):
        return f' {self.first_name}  {self.last_name} {self.age} {self.city} {self.rating} '