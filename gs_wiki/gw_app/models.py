from django.db import models

# Create your models here.
class Char(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    star = models.CharField(max_length=2)
    element = models.CharField(max_length=2)
    type = models.CharField(max_length=20)
    area = models.CharField(max_length=10)
    brithday = models.CharField(max_length=10)
    brith_date = models.DateField(default='2020-09-28')
    affiliation = models.CharField(max_length=16)
    constell = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    bvid = models.CharField(max_length=64, null=True)
    material_day = models.IntegerField(default=1)
    material_area = models.CharField(max_length=10)
    debut_version = models.CharField(max_length=4, default='1.0')
    up_start = models.DateField(null=True)
    up_end = models.DateField(null=True)


class BaseAttr(models.Model):
    # value: 'value1, value2, ..., valueN'
    char = models.ForeignKey(Char, on_delete=models.CASCADE)
    baseHP = models.CharField(max_length=128)   # value
    baseATK = models.CharField(max_length=128)  # value
    baseDEF = models.CharField(max_length=128)  # value
    ascend_attr_label = models.CharField(max_length=16)
    ascend_attr_value = models.CharField(max_length=128)    # value


class TalentInfo(models.Model):
    char = models.ForeignKey(Char, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()


class TalentVal(models.Model):
    # value: 'value1, value2, ..., valueN'
    talent = models.ForeignKey(TalentInfo, on_delete=models.CASCADE)
    label = models.CharField(max_length=20)
    value = models.CharField(max_length=512)    # value


class Constellation(models.Model):
    char = models.ForeignKey(Char, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()


class Story(models.Model):
    char = models.ForeignKey(Char, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()


class VoiceOver(models.Model):
    char = models.ForeignKey(Char, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.TextField()


class Weapon(models.Model):
    # value: 'value1, value2, ..., valueN'
    name = models.CharField(max_length=20)
    star = models.CharField(max_length=2)
    type = models.CharField(max_length=20)
    baseATK = models.CharField(max_length=128)  # value
    sub_label = models.CharField(max_length=20, null=True)
    sub_value = models.CharField(max_length=128, null=True)    # value
    effect_title = models.CharField(max_length=20, null=True)
    effect_text = models.TextField(null=True)
    description = models.CharField(max_length=128)
    story = models.TextField()
    material_day = models.IntegerField(default=1)
    material_area = models.CharField(max_length=10)
    debut_version = models.CharField(max_length=4, default='1.0')
    up_start = models.DateField(null=True)
    up_end = models.DateField(null=True)


class Version(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=4)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class GachaPool(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    img = models.CharField(max_length=64)
    link = models.CharField(max_length=20)
