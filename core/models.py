from django.db import models


class Team(models.Model):
    name = models.CharField('Name', max_length=32)
    label = models.CharField('Label', max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Sprint(models.Model):
    number = models.IntegerField('Number')
    start_date = models.DateTimeField('Start Date', blank=True, null=True)
    finish_date = models.DateTimeField('Finish Date', blank=True, null=True)

    def __unicode__(self):
        return 'Sprint {number}'.format(number=self.number)

    class Meta:
        ordering = ('number',)
