from django.db import models


class WordStok(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.word


