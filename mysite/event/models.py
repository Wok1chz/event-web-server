from django.db import models
from django.urls import reverse, reverse_lazy
from django import template


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    type = models.CharField(max_length=255, verbose_name="Тип", choices={
            ('Online', 'Online'),
            ('Offline', 'Offline'),
    })
    logo = models.ImageField(upload_to="logo", verbose_name="Логотип")
    date_start = models.DateField(verbose_name="Дата начала мероприятия")
    date_end = models.DateField(verbose_name="Дата окончания мероприятия")
    city = models.CharField(max_length=255, verbose_name="Город")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'
        # ordering = ['date_end', 'title']


class EventUser(models.Model):
    event = models.ForeignKey('Event', on_delete=models.PROTECT, null=True)
    user_id = models.IntegerField()
    logo = models.ImageField(upload_to="logo")
    date_join = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def has_sign(user_id, event_id):
        if EventUser.objects.filter(user_id=user_id, event_id=event_id):
            return True
        else:
            return False



