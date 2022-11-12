from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=200, verbose_name='Описание датчика')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура при измерении')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['created_at']

    def __str__(self):
        return f'Дата измерения: {self.created_at}, Температура: {self.temperature}'
