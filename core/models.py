from django.db import models

class Faction(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фракции')
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание')

    def __str__(self):
        return self.name

class FactionDescription(models.Model):
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE, related_name='factiondescription', verbose_name='Фракция')
    full_description = models.TextField(verbose_name='Полное описание')

    def __str__(self):
        # return self.faction.name
        return f"Описание {self.faction.name}"

class Metro(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название метрополитена')
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название станции')
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, related_name='stations', verbose_name='Метро')

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя персонажа')
    factions = models.ManyToManyField(Faction, related_name='characters', verbose_name='Фракции')
    image = models.ImageField(upload_to='characters/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name