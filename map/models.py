from django.contrib.postgres.indexes import GinIndex
from django.db import models


class Map(models.Model):
    created_by = models.ForeignKey('member.Member', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    description = models.TextField()
    main_image_url = models.TextField(blank=True, null=True)
    subscribed_count = models.BigIntegerField(
        default=0,
        help_text='현재 구독 수',
        db_index=True,
    )
    once_subscribed_count = models.BigIntegerField(
        default=0,
        help_text='지금까지 구독 수',
        db_index=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            GinIndex(
                fields=['title'],
                name='title_gin_idx',
                opclasses=['gin_trgm_ops'],
            ),
        ]
        verbose_name = '맵'
        verbose_name_plural = '맵'

    def __str__(self):
        return f'id: {self.id} / title: {self.title}'
