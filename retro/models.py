from django.db import models
from model_choices import *


class Sticker(models.Model):
    created = models.DateTimeField('Creation Date', auto_now_add=True)
    summary = models.CharField('Description', max_length=1024, null=True, blank=True)
    type = models.CharField('type', max_length=1, choices=STICKER_TYPE_CHOICES, default=STICKER_TYPE_CHANGE)
    status = models.CharField('status', max_length=1, choices=STICKER_STATUS_CHOICES, default=STICKER_STATUS_CREATED)
    owner = models.ForeignKey('auth.User', related_name='stickers')
    board = models.ForeignKey('retro.Board', related_name='stickers')

    def __unicode__(self):
        return '{summary} ({owner}, {team})'.format(summary=self.summary[:25], owner=self.owner, team='team')

    class Meta:
        ordering = ('created',)


class Board(models.Model):
    created = models.DateTimeField('Creation Date', auto_now_add=True)
    isActive = models.BooleanField('Is Active', default=False)
    voteLimit = models.IntegerField('Vote Limit', default=3)
    owner = models.ForeignKey('auth.User', related_name='boards')
    team = models.ForeignKey('core.Team', related_name='boards')
    sprint = models.ForeignKey('core.Sprint', related_name='boards')

    def __unicode__(self):
        return '{team} sprint {sprint}'.format(team=self.team.name, sprint=self.sprint.number)

    class Meta:
        ordering = ('created',)