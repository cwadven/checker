from django.contrib.auth.models import AbstractUser
from django.db import models
from member.consts import (
    AcquisitionPKType,
    MemberStatusExceptionTypeSelector,
)
from member.managers import MemberManager


class MemberProvider(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MemberStatus(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MemberType(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Member(AbstractUser):
    nickname = models.CharField(max_length=45, blank=True, null=True, db_index=True, unique=True)
    member_type = models.ForeignKey(MemberType, models.DO_NOTHING, blank=True, null=True)
    member_status = models.ForeignKey(MemberStatus, models.DO_NOTHING, blank=True, null=True)
    member_provider = models.ForeignKey(MemberProvider, models.DO_NOTHING, blank=True, null=True)
    profile_image_url = models.CharField(max_length=256, blank=True, null=True)

    objects = MemberManager()

    class Meta:
        verbose_name = '일반 사용자'
        verbose_name_plural = '일반 사용자'

    def raise_if_inaccessible(self):
        if self.member_status_id != 1:
            raise MemberStatusExceptionTypeSelector(self.member_status_id).selector()


class Guest(models.Model):
    u"""
    email: 내가 비회원으로 뭔가 했던 기준을 찾기 위해서
    """
    temp_nickname = models.CharField(max_length=45, unique=True, db_index=True)
    ip = models.CharField(max_length=256, blank=True, null=True, db_index=True)
    email = models.EmailField(max_length=256, blank=True, null=True, db_index=True)
    member = models.OneToOneField(Member, models.DO_NOTHING, blank=True, null=True)
    is_blacklisted = models.BooleanField(default=False)
    blacklist_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    last_joined_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = '비회원'
        verbose_name_plural = '비회원'

    def __str__(self):
        return self.temp_nickname


class MemberInformation(models.Model):
    member = models.ForeignKey(Member, models.DO_NOTHING)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = '회원 정보'
        verbose_name_plural = '회원 정보'

    def __str__(self):
        return f'{self.member_id, self.description[:20]}'


class MemberExtraLink(models.Model):
    member = models.ForeignKey(Member, models.DO_NOTHING)
    url = models.TextField()
    title = models.TextField()
    description = models.TextField()
    sequence = models.IntegerField(blank=True, null=True, db_index=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = '회원 링크'
        verbose_name_plural = '회원 링크'

    def __str__(self):
        return f'{self.member_id, self.title}'


class MemberMapSubscription(models.Model):
    member = models.ForeignKey(Member, models.DO_NOTHING)
    map = models.ForeignKey('map.Map', models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '회원 맵 구독'
        verbose_name_plural = '회원 맵 구독'

    def __str__(self):
        return f'member: {self.member_id} / map_id: {self.map_id}'


class MemberNodeAcquisition(models.Model):
    member_map_subscription = models.ForeignKey(
        MemberMapSubscription,
        models.DO_NOTHING,
    )
    map = models.ForeignKey('map.Map', models.DO_NOTHING)
    node = models.ForeignKey('network.Node', models.DO_NOTHING)
    acquisition_pk = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
    )
    acquisition_pk_type = models.CharField(
        max_length=256,
        choices=AcquisitionPKType.choices(),
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '회원 Node 획득'
        verbose_name_plural = '회원 Node 획득'

    def __str__(self):
        return f'member: {self.member_map_subscription.member_id} / node_id: {self.node_id}'


class MemberArrowAcquisition(models.Model):
    member_map_subscription = models.ForeignKey(
        MemberMapSubscription,
        models.DO_NOTHING,
    )
    map = models.ForeignKey('map.Map', models.DO_NOTHING)
    arrow = models.ForeignKey('network.Arrow', models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '회원 Arrow 획득'
        verbose_name_plural = '회원 Arrow 획득'

    def __str__(self):
        return f'member: {self.member_map_subscription.member_id} / arrow_id: {self.arrow_id}'
