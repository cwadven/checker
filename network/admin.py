from django.contrib import admin
from network.models import (
    Arrow,
    ArrowAcquisitionQuestionAnswer,
    ArrowAcquisitionQuestionMemberResponse,
    ArrowAcquisitionQuestionMemberResponseReply,
    ArrowAcquisitionQuestionRule,
    ArrowAcquisitionRule,
    Node,
    NodeAcquisitionRule,
)


class NodeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'map',
        'created_by',
        'simple_word',
        'title',
        'description',
        'is_acquisition_only_show_info',
        'phase',
        'size',
        'total_acquisition_count',
        'is_deleted',
    ]


class NodeAcquisitionRuleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'node',
        'title',
        'is_deleted',
    ]


class ArrowAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'created_by',
        'simple_word',
        'title',
        'description',
        'is_acquisition_only_show_info',
        'total_acquisition_count',
        'source_node',
        'target_node',
        'is_deleted',
    ]


class ArrowAcquisitionRuleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'arrow',
        'is_deleted',
    ]


class ArrowAcquisitionQuestionRuleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'arrow_acquisition_rule',
        'is_auto_mark',
        'is_always_correct',
        'is_deleted',
    ]


class ArrowAcquisitionQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'arrow_acquisition_question_rule',
        'answer',
        'is_deleted',
    ]


class ArrowAcquisitionQuestionMemberResponseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'arrow_acquisition_question_rule',
        'member_map_subscription',
        'response',
        'status',
        'question_member_response_reply',
        'is_deleted',
    ]


class ArrowAcquisitionQuestionMemberResponseReplyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'arrow_acquisition_question_member_response',
        'replied_member',
        'reply',
        'replied_status',
        'is_deleted',
    ]


admin.site.register(Node, NodeAdmin)
admin.site.register(Arrow, ArrowAdmin)
admin.site.register(NodeAcquisitionRule, NodeAcquisitionRuleAdmin)
admin.site.register(ArrowAcquisitionRule, ArrowAcquisitionRuleAdmin)
admin.site.register(ArrowAcquisitionQuestionRule, ArrowAcquisitionQuestionRuleAdmin)
admin.site.register(ArrowAcquisitionQuestionAnswer, ArrowAcquisitionQuestionAnswerAdmin)
admin.site.register(ArrowAcquisitionQuestionMemberResponse, ArrowAcquisitionQuestionMemberResponseAdmin)
admin.site.register(ArrowAcquisitionQuestionMemberResponseReply, ArrowAcquisitionQuestionMemberResponseReplyAdmin)
