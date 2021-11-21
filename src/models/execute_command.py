from commands import command_factory

# 共通バリデーション
def validation(data: dict)->bool:
    if 'name' not in data:
        return False

    return True

def execute(data:dict)->dict:
    if validation(data=data) == False:
        raise Exception("不正アクセス")

    command_name = data.get('name')

    options = {}
    if 'options' in data:
        options = {v['name']: v['value'] for v in data.get('options')}

    command = command_factory.create(command_name=command_name)

    command.validate(options=options)

    return command.execute(options=options)
