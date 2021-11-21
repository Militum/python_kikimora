
import constants
from commands import CommandBase

class HelpCommand(CommandBase):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, member: dict, options: dict) -> None:
        super().validate(member, options)

    def execute(self, member: dict, options: dict)->dict:
        help_text = '★忙しすぎるあなたに代わって教室を作成します。\n' \
            '全てのコマンドには入力補助がつきますのでご安心下さい。\n\n' \
            '** ● 募集を立てたいとき ● **\n' \
            '> `/recruit チャンネル名`と発言してください。\n' \
            '** ● セッションチャンネルを立てたいとき ● **\n' \
            '> `/room チャンネル名`と発言してください。\n' \
            '** ● キャンペーン用のチャンネルを立てたいとき ● **\n' \
            '> `/campaign チャンネル名`と発言してください。\n' \
            '** ● チャンネル名を変更したいとき ● **\n' \
            '> `/rename 新しいチャンネル名`と発言してください。\n' \
            '** ● チャンネル名の頭に「〆」をつけたいとき または外したいとき● **\n' \
            '> `/close` と発言してください（発言するたびに「〆」が着脱されます。連続実行時の制限に注意）。\n' \
            '** ● チャンネルの削除を行いたいとき ● **\n' \
            '> `/delete`と発言してください。\n\n' \
            '** ● 作成したチャンネルに他のユーザーを誘いたいとき ● **\n' \
            '※教室の名前については、サーバのルールに準拠するようにしてください。'

        return {
            "type": constants.RESPONSE_TYPES['MESSAGE_WITH_SOURCE'],
            "data": {
                "content": help_text
            }
        }
