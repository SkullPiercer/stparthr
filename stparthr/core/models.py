from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='streets'
    )

    class Meta:
        unique_together = ('name', 'city')

    def __str__(self):
        return f"{self.name}, {self.city.name}"


class Shop(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='shops'
    )
    street = models.ForeignKey(
        Street, on_delete=models.CASCADE, related_name='shops'
    )
    house_number = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        unique_together = ('name', 'city', 'street', 'house_number')

    def __str__(self):
        return (
            f"{self.name} ({self.city.name},"
            f" {self.street.name} {self.house_number})"
        )
