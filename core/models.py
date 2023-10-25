from django.db import models
from .constants import *

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='product_pictures/', verbose_name="Картинка")
    content = models.TextField(null=True, verbose_name="Контент")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return f"Product (id = {self.id}, name = {self.name})"


class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итоговая сумма")
    status = models.IntegerField(
        choices=ORDER_STATUS_CHOISES,
        default=order_status_new,
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    confirmed_at = models.DateTimeField(null=True, blank=True, verbose_name="Время подтверждения")
    products = models.ManyToManyField(Product, related_name="product_order", verbose_name="Товары")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return f"Order (id = {self.id}, amount = {self.amount}, status = {self.status})"


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    status = models.IntegerField(
        choices=PAYMENT_STATUS_CHOISES,
        default=payment_status_new,
        verbose_name="Статус",
    )
    payment_type = models.IntegerField(
        choices=PAYMENT_TYPE_CHOISES,
        default=payment_type_cash,
        verbose_name="Тип оплаты"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self) -> str:
        return f"Payment (id = {self.id}, amount = {self.amount}, status = {self.status}, payment_type = {self.payment_type})"
