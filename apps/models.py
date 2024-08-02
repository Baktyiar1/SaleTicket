from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
class Ticket(models.Model):
    title = models.CharField(
        'Название',
        max_length=150
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Стоимость'
    )
    location_event = models.CharField(
        'Место проводение',
        max_length=150
    )
    image = models.ImageField(
        'Изображение',
        upload_to='media/images/'
    )
    event_date = models.DateTimeField(
        verbose_name='Дата мероприятия'
    )
    date_duration = models.CharField(
        max_length= 50,
        verbose_name='Продолжительность'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Кол-во билетов'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность'
    )
    create_date = models.DateTimeField(
        'Дата создание объекта',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        'Дата обновление',
        auto_now=True
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,

        verbose_name='Пользователь'
    )

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.PROTECT,

        verbose_name='Билет'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Кол-во билетов'
    )
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Стоимость'
    )
    status = models.PositiveSmallIntegerField(
        choices=[
            (1, 'Заказ обработке'),
            (2, 'Заказ оплачен'),
            (3, 'Заказ отменен')

        ],
        default=1,
        verbose_name='Статус'
    )
    create_date = models.DateTimeField(
        'Дата создание объекта',
        auto_now_add=True
    )

    def __str__(self):
        return str(self.user)

