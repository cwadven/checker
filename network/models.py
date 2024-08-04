from django.contrib.postgres.indexes import GinIndex
from django.db import models
from network.consts import (
    NodePhase,
    QuestionMemberResponseStatus,
)


class Node(models.Model):
    map = models.ForeignKey('map.Map', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey('member.Member', on_delete=models.DO_NOTHING)
    simple_word = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_acquisition_only_show_info = models.BooleanField(default=False)
    phase = models.CharField(
        max_length=20,
        choices=NodePhase.choices(),
        null=True,
    )
    size = models.FloatField(default=1.0)
    total_acquisition_count = models.BigIntegerField(
        default=0,
        help_text='총 획득 수',
        db_index=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            GinIndex(
                fields=['simple_word'],
                name='node_simple_word_gin_idx',
                opclasses=['gin_trgm_ops'],
            ),
            GinIndex(
                fields=['title'],
                name='node_title_gin_idx',
                opclasses=['gin_trgm_ops'],
            ),
        ]

    def __str__(self):
        return f'id: {self.id} / simple_word: {self.simple_word}'


class Arrow(models.Model):
    created_by = models.ForeignKey('member.Member', on_delete=models.DO_NOTHING)
    simple_word = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_acquisition_only_show_info = models.BooleanField(default=False)
    total_acquisition_count = models.BigIntegerField(
        default=0,
        help_text='총 획득 수',
        db_index=True,
    )
    source_node = models.ForeignKey(
        'Node',
        on_delete=models.DO_NOTHING,
        related_name='source_arrows',
        help_text='출발지 노드',
    )
    target_node = models.ForeignKey(
        'Node',
        on_delete=models.DO_NOTHING,
        related_name='target_arrows',
        help_text='도착지 노드',
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NodeAcquisitionRule(models.Model):
    node = models.ForeignKey('Node', on_delete=models.DO_NOTHING)
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    arrows = models.ManyToManyField(
        'Arrow',
        blank=True,
        null=True,
        help_text='노드 획득을 위한 필요한 획득 Arrow',
    )

    def __str__(self):
        return f'id: {self.id} / node_id: {self.node_id} / title: {self.title}'


class ArrowAcquisitionRule(models.Model):
    arrow = models.ForeignKey('Arrow', on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} / arrow_id: {self.arrow_id}'


class ArrowAcquisitionQuestionRule(models.Model):
    arrow_acquisition_rule = models.ForeignKey('ArrowAcquisitionRule', on_delete=models.DO_NOTHING)
    question = models.TextField()
    is_auto_mark = models.BooleanField(default=False)
    is_always_correct = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} / arrow_acquisition_rule_id: {self.arrow_acquisition_rule_id}'


class ArrowAcquisitionQuestionAnswer(models.Model):
    arrow_acquisition_question_rule = models.ForeignKey('ArrowAcquisitionQuestionRule', on_delete=models.DO_NOTHING)
    answer = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} / arrow_acquisition_question_rule_id: {self.arrow_acquisition_question_rule_id}'


class ArrowAcquisitionQuestionMemberResponse(models.Model):
    arrow_acquisition_question_rule = models.ForeignKey('ArrowAcquisitionQuestionRule', on_delete=models.DO_NOTHING)
    member_map_subscription = models.ForeignKey('member.MemberMapSubscription', on_delete=models.DO_NOTHING)
    response = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=QuestionMemberResponseStatus.choices(),
    )
    question_member_response_reply = models.ForeignKey(
        'ArrowAcquisitionQuestionMemberResponseReply',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} / arrow_acquisition_question_rule_id: {self.arrow_acquisition_question_rule_id}'


class ArrowAcquisitionQuestionMemberResponseReply(models.Model):
    arrow_acquisition_question_member_response = models.ForeignKey('ArrowAcquisitionQuestionMemberResponse', on_delete=models.DO_NOTHING)
    replied_member = models.ForeignKey('member.Member', on_delete=models.DO_NOTHING)
    reply = models.TextField(
        null=True,
        blank=True,
    )
    replied_status = models.CharField(
        max_length=20,
        choices=QuestionMemberResponseStatus.choices(),
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id: {self.id} / arrow_acquisition_question_member_response_id: {self.arrow_acquisition_question_member_response_id}'
