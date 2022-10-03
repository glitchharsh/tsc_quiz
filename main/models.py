from django.db import models

# Create your models here.


class QuizModel(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}: {self.score}"
    
