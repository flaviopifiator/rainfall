from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        return cls.objects.first()
    
    def save(self, *args, **kwargs):
        if not self._meta.model.objects.count():
            super().save(*args, **kwargs)
        if self.pk:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
