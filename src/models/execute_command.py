from commands import help_command

# 共通バリデーション
def validation(options: dict)->bool:
    if 'name' not in options:
        return False

    return True

def execute(options:dict)->dict:
    if validation(options) == False:
        raise Exception("不正アクセス")

    # どれにも当てはまらない場合はhelpコマンドと見做す
    return help_command.execute(options=options)
