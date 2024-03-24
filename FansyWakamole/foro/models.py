from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    Comentario = models.TextField()
    Puntuaciones_Choises = (
        (1,"⭐"),
        (2,"⭐⭐"),
        (3,"⭐⭐⭐"),
        (4,"⭐⭐⭐⭐"),
        (5,"⭐⭐⭐⭐⭐"),
    )
    Puntuacion = models.IntegerField(choices=Puntuaciones_Choises, default=1)
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    def __str__(self):
        if self.title:
            return self.title
        else:
            return f"Post de {self.Nombre}"

class Comentario(models.Model):
    text = models.CharField(max_length=250)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)

    def __str__(self):
        if self.text:
            return self.text
        else:
            return f"Comentario de {self.Nombre}"

