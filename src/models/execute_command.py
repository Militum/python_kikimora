from commands import command_factory

# 共通バリデーション
def validation(member:dict, data: dict)->bool:
    if 'user' not in member:
        return False

    if 'name' not in data:
        return False

    return True

def execute(member:dict, data:dict)->dict:
    if validation(member=member, data=data) == False:
        raise Exception("不正アクセス")

    command_name = data.get('name')

    options = {}
    if 'options' in data:
        options = {v['name']: v['value'] for v in data.get('options')}

    command = command_factory.create(command_name=command_name)

    command.validate(member=member, options=options)

    return command.execute(member=member, options=options)
