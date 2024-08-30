from django.db import models
from django.utils.text import slugify

class ImgApp(models.Model):
    image = models.URLField(max_length=1000, editable=False)
    card_title = models.CharField(max_length=50)
    card_description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.card_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.card_title


class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ImgAppDb(models.Model):
    image = models.FileField(upload_to='images/', max_length=100)
    card_title = models.CharField(max_length=50)
    card_description = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=255, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(TagLine,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.card_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.card_title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(ImgAppDb, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"