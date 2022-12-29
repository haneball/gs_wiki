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
    affiliation = models.CharField(max_length=16)
    constell = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    bvid = models.CharField(max_length=64, null=True)


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
    telent = models.ForeignKey(TalentInfo, on_delete=models.CASCADE)
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
