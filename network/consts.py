from common.common_consts.common_enums import StrValueLabel


class NodePhase(StrValueLabel):
    START = ('START', '시작')
    END = ('END', '종료')


class QuestionMemberResponseStatus(StrValueLabel):
    PENDING = ('PENDING', '답변중')
    CORRECT = ('CORRECT', '정답')
    WRONG = ('WRONG', '오답')
