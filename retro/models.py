from django.db import models
from model_choices import *


class Sticker(models.Model):
    created = models.DateTimeField('Creation Date', auto_now_add=True)
    summary = models.CharField('Description', max_length=1024, null=True, blank=True)
    type = models.CharField('type', max_length=1, choices=STICKER_TYPE_CHOICES, default=STICKER_TYPE_CHANGE)
    rating = models.PositiveIntegerField('Rating', default=0)
    advanced_status = models.ForeignKey('retro.StickerAdvancedStatus', related_name='advanced_status')
    owner = models.ForeignKey('auth.User', related_name='stickers')
    board = models.ForeignKey('retro.Board', related_name='stickers')

    def __unicode__(self):
        return '{summary} ({owner}, {team}, Sprint {sprint})'.format(summary=self.summary[:25],
                                                                     owner=self.owner,
                                                                     team=self.board.team.name,
                                                                     sprint=self.board.sprint.number)

    class Meta:
        ordering = ('-created',)


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


class StickerAdvancedStatus(models.Model):
    name = models.CharField('Name', max_length=32)
    description = models.CharField('Description', max_length=64)
    priority = models.PositiveSmallIntegerField('Priority', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('priority',)