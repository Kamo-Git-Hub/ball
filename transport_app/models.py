# -*- coding: utf-8 -*-
# !/usr/bin/env python
from django.db import models


class RegionModel(models.Model):
    region_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.region_name}'

    class Meta:
        verbose_name = "Տարածաշրջան"
        verbose_name_plural = "Տարածաշրջան"


class RegionChildModel(models.Model):
    region_child = models.CharField(max_length=55, verbose_name='Поселение')
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, verbose_name='Регион')

    def __str__(self):
        return f'{self.region_child}'

    class Meta:
        verbose_name = "Տարածաշրջան-Raion"
        verbose_name_plural = "Տարածաշրջան-Raion"


class ManufacturerCountry(models.Model):
    man_country = models.CharField(max_length=30, verbose_name='Manufacturer country')

    def __str__(self):
        return self.naman_country

    class Meta:
        verbose_name = "Արտադրման երկիր"
        verbose_name_plural = "Արտադրման երկիր"


class CarBrand(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='Brand')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Մակնիշ"
        verbose_name_plural = "Մակնիշ"


class CarModel(models.Model):
    model_name = models.CharField(max_length=30, verbose_name='MOdel name')
    category = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "Մոդել"
        verbose_name_plural = "Մոդել"


class CarBody(models.Model):
    car_body = models.CharField(max_length=32, verbose_name="tapki tesak")

    def __str__(self):
        return self.car_body

    class Meta:
        verbose_name = "Թափքի տեսակ"
        verbose_name_plural = "Թափքի տեսակ"


class ProductYear(models.Model):
    product_year = models.CharField(max_length=32)

    def __str__(self):
        return self.product_year

    class Meta:
        verbose_name = "Տարի"
        verbose_name_plural = "Տարի"


class Fuel(models.Model):
    fuel_type = models.CharField(max_length=32)

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = "Վառելիք"
        verbose_name_plural = "Վառելիք"


class Motor(models.Model):
    motor = models.CharField(max_length=32)

    def __str__(self):
        return self.motor

    class Meta:
        verbose_name = "Շարժիչի ծավալ"
        verbose_name_plural = "Շարժիչի ծավալ"


class Transmission(models.Model):
    transmission = models.CharField(max_length=32)

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = "Փոխանցման տուփ"
        verbose_name_plural = "Փոխանցման տուփ"


class Clearance(models.Model):
    clearance = models.CharField(max_length=32)

    def __str__(self):
        return self.clearance

    class Meta:
        verbose_name = "Մաքսազերծված է"
        verbose_name_plural = "Մաքսազերծված է"


class Steering(models.Model):
    steering = models.CharField(max_length=32)

    def __str__(self):
        return self.steering

    class Meta:
        verbose_name = "Ղեկ"
        verbose_name_plural = "Ղեկ"


class Color(models.Model):
    color = models.CharField(max_length=32)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Գույն"
        verbose_name_plural = "Գույն"


class DriveUnit(models.Model):
    drive_unit = models.CharField(max_length=32)

    def __str__(self):
        return self.drive_unit

    class Meta:
        verbose_name = "Քարշակ"
        verbose_name_plural = "Քարշակ"


class AutoModel(models.Model):
    class ChoiceType(models.TextChoices):
        KM = 'km'
        ML = 'ml'

    class ChoiceDescLanguage(models.TextChoices):
        AM = 'ARM'
        RU = 'RUS'
        EN = 'EN'

    class ChoiceContact(models.TextChoices):
        WHATSAPP = 'whatsapp'
        VIBER = 'viber'
        TELEGRAM = 'telegram'
        ZANGI = 'zangi'

    vin_code = models.CharField(max_length=32, unique=True, blank=True, null=True)
    show_vin_code = models.BooleanField(default=True)
    region_name = models.ForeignKey(RegionModel, on_delete=models.CASCADE)
    region_child = models.ForeignKey(RegionChildModel, on_delete=models.CASCADE)
    man_country = models.ForeignKey(ManufacturerCountry, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_body = models.ForeignKey(CarBody, on_delete=models.CASCADE)
    product_year = models.OneToOneField(ProductYear, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    clearance = models.ForeignKey(Clearance, on_delete=models.CASCADE)
    steering = models.ForeignKey(Steering, on_delete=models.CASCADE)
    new = models.BooleanField(default=False, verbose_name='Նոր')
    used = models.BooleanField(default=False, verbose_name='Օգտագործված')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    drive_unit = models.ForeignKey(DriveUnit, on_delete=models.CASCADE)
    horse_power = models.IntegerField(verbose_name='Ձիաուժ')
    millage_int = models.IntegerField(verbose_name='Վազք')
    mileage = models.CharField(max_length=50, choices=ChoiceType.choices, default=ChoiceType.KM,
                               verbose_name='Վազք-type')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Գին')
    photo_main = models.ImageField(upload_to='photos/transport/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/transport/%Y/%m/%d/', blank=True)
    mileage = models.CharField(max_length=50, choices=ChoiceDescLanguage.choices,
                               default=ChoiceDescLanguage.AM)
    description = models.TextField( verbose_name='Նկարագրել')
    hashtag = models.CharField(max_length=255, blank=True, verbose_name='Գաղտնի որոնում')
    contact = models.CharField(max_length=33, verbose_name='Կոնտակտ')
    contact_type = models.CharField(max_length=32, choices=ChoiceContact.choices,
                                    verbose_name='Կոնտակտ_type')
    exchange = models.BooleanField(default=False, verbose_name='Փոխանակում')
    dealer = models.BooleanField(default=False, verbose_name='Դիլլեր')
    created_at = models.DateTimeField(auto_now=True, verbose_name='don`t tuch)')

    def __str__(self):
        return str('Auto Model')

    class Meta:
        verbose_name = "Transport"
        verbose_name_plural = "Transports"
