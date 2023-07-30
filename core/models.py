from django.db import models


# Create your models here.


class BaseAbstractModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated At',
        blank=True,
        auto_now=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Created At',
        blank=True,
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def natural_key(self):
        return {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
