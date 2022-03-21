# python_kikimora

## [kikimora](https://github.com/kotobukid/kikimora)のAWSLambda対応版

### 必要な環境変数
|変数名|意味|備考|
|--|--|--|
|DISCORD_PUBLIC_KEY|discord public key||
|DISCORD_TOKEN|discord bot token||
|APPLICATION_ID|discord application id||
|COMMAND_GUILD_ID|実行するDiscordチャンネル|公開Botにするなら要修正|
|RECRUIT_CATEGORY_ID|募集チャンネルを作成するカテゴリー||
|SESSION_TEXT_CATEGORY_ID|ワンオフセッションのテキストチャンネルを作成するカテゴリー||
|SESSION_VC_CATEGORY_ID|ワンオフセッションのボイスチャンネルを作成するカテゴリー||
|CAMPAIGN_TEXT_CATEGORY_ID|キャンペーンのテキストチャンネルを作成するカテゴリー||
|CAMPAIGN_VC_CATEGORY_ID|キャンペーンのボイスチャンネルを作成するカテゴリー||

### 実行可能なコマンド

* セッションの募集チャンネルを作成します  
    コマンド:`/recruit channnel_name`  
    `channnel_name`:作成するチャンネル名

* セッションの募集を締め切ります(既に締め切っている場合は再Openします)  
    コマンド:`/close`  

* セッションチャンネルを作成します  
    コマンド:`/room channnel_name is_oneoff (is_voice_session)`  
    `channnel_name`:作成するチャンネル名  
    `is_oneoff`:ワンオフの場合はTrue、キャンペーンの場合はFalse  
    `is_voice_session`:ボイスセッションの場合はTrue、テキストのみはFalse。デフォルトはボイスセッション

* セッションチャンネルを削除します  
    コマンド:`/delete`  
    todo:チャンネル作成者との紐付けが必要

* 使い方を表示します  
    コマンド:`/help`
