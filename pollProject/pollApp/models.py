from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=255)
    pub_date=models.DateTimeField('publishing date')

    def __str__(self):
        return self.question_text