from django.db import models

class Block(models.Model):
    class Meta:
        verbose_name = "Текстовый блок"
        verbose_name_plural = "Текстовые блоки"
    code = models.CharField(verbose_name="Код", max_length=250, unique=True)
    text = models.TextField(verbose_name="Текст")
