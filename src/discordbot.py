# インストールした discord.py を読み込む
import discord
from googlesearch import search
import csv
import random
from discord.ext import tasks
#from discord.ext import commands
from datetime import datetime 
#from typing import Dict
#from dbot.core.bot import DBot
#from googletrans import Translator
#import datetime
# from time import sleep
import asyncio
import tokenset
# 自分のBotのアクセストークンに置き換えてください
TOKEN = tokenset.get_token()

foxbot_path = "/Users/akagamiaozora/Documents/統合ゼミコミュニティ/foxbot.csv"
keyword_path = "/Users/akagamiaozora/Documents/統合ゼミコミュニティ/keyword.csv"

# 接続に必要なオブジェクトを生成
client = discord.Client()
# translator = Translator()
#pretime_dict = {}
#bot = commands.Bot(command_prefix="/")

ModeFlag = 0
Flag = 0
PFlag = 0
q = []
pf = 0
pcomo = 0

global_channel_name = "グローバルチャット"
shintyoku = "🐦｜統合進捗報告"


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await client.change_presence(activity=discord.Game("もっふもっふたいむ"))

@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return

    # if message.content == "~join":
    #     if message.author.voice is None:
    #         await message.channel.send("あなたはボイスチャンネルに接続していません。")
    #         return
    #     # ボイスチャンネルに接続する
    #     await message.author.voice.channel.connect()
    #     await message.channel.send("接続しました。")

    # elif message.content == "~leave":
    #     if message.guild.voice_client is None:
    #         await message.channel.send("接続していません。")
    #         return

    #     # 切断する
    #     await message.guild.voice_client.disconnect()

    #     await message.channel.send("切断しました。")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global ModeFlag
    global Flag
    global pflag
    global pcomo
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/fox」と発言したら"(^・ω・^)ノ こやーん"が返る処理
    if message.content == '/santa':
        await message.channel.send('(^・ω・^)ノ こやーん（サンタさんは今どこかな？）\n https://santatracker.google.com/?utm_source=google&utm_medium=hpp&utm_campaign=Global')

    with open(foxbot_path) as f:
        reader = csv.reader(f)
        semi_name = [row for row in reader]

    with open(keyword_path) as f:
        reader = csv.reader(f)
        key_list = [row for row in reader]

    semi_list = ["" for _ in range(len(semi_name))]

    for i in range(len(semi_name)):
        semi_list[i] = semi_name[i][1] + "\nチャンネルはこちら→" + semi_name[i][2] + "\n Notionのページはこちら→" + semi_name[i][3]


    # key_list = [['物理', '数理物理学', '数理物理'], 
    #             ['物理', '杉山相対性理論', '相対論', '相対性理論ゼミ'],
    #             ['物理', '流体力学'],
    #             ['数学', '集合位相'],
    #             ['院試', '演習'],
    #             ['数学', 'Coq', 'coq'],
    #             ['古事記'],
    #             ['数学', '確率'],
    #             ['物理', '統計力学'],
    #             ['情報', 'プログラミング', 'ディープラーニング', '深層学習'],
    #             ['地学', '気象'],
    #             ['物理', '堀田', '量子力学'],
    #             ['生物', 'ヴォート', 'essentila', 'ワトソン', '生化学', '遺伝'],
    #             ['情報', 'プログラミング', '数値計算', 'もくもく'],
    #             ['音響', '音'],
    #             ['情報', 'プログラミング', 'Python', 'python', '数学'],
    #             ['fromkin'],
    #             ['語学', 'ラテン語', '錬金術'],
    #             ['物理', '解析力学'],
    #             ['情報', 'haskell', 'プログラミング'],
    #             ['音', 'プログラミング', 'Python', 'python'],
    #             ['語学', 'TOEIC'],
    #             ['情報', 'IT'],
    #             ['数学', '物理', 'ベクトル'],
    #             ['数学', '多様体'],
    #             ['物理', '量子', '情報'],
    #             ['物理', '力学'],
    #             ['百人一首'],
    #             ['一覧', '全部', 'all', 'カレンダー']
    #             ]
    # semi_list = ["数理物理学ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/764852349595287553/764852591074082866", 
    #             "杉山相対性理論ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/836873517143293952/837971413699657728",
    #             '流体力学ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/837970240452427817/837972887654105118',
    #             '松坂集合位相ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/839118836330397737/861196065210236938',
    #             '院試・演習勉強会 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/839156458338779158/888062408931831809',
    #             'Coqゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/764841858990997515/839791164398895145', 
    #             '古事記輪読会 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/840433471411060760/840827482076086273',
    #             '確率解析ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/841646702401552454/841690198643048478',
    #             '田崎統計力学ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/852528083914457138/852529470446895124',
    #             'ディープラーニングゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/855354313773940736/855367886083325952',
    #             '気象学ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/865232350680973332/868108279690174515',
    #             '堀田量子力学ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/874563054644383794/874601884332228660',
    #             '生物輪読ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/874952362253500416/874955197925974026',
    #             '数値計算 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/875364753550233670/875365717116063784',
    #             '音響工学原論 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/875364814367641641/875365858938060831',
    #             'Pythonから始める数学入門 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/875364905535025253/875365933647028234',
    #             'fromkinを読む会 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/875657083020804126/875657436604813363',
    #             'ラテン語・錬金術ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/877538794600017920/877539780907368518',
    #             '解析力学 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/879325817937735680/879326057113747487', 
    #             'Haskellゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/879228427910135838/879230967083040798',
    #             'Pythonで学ぶ音源分離音声認識音声合成 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/879508345877303347/879528044770000916',
    #             'toeic-lr攻略会 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/880019752020496414/880020195266158603',
    #             'ITパスポート勉強会 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/884081969955229797/884096022731710514',
    #             'シン・ベクトル解析ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/884081969955229797/884096022731710514',
    #             '多様体の基礎ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/881780718181699615/881781065184862248',
    #             '量子情報ゼミ \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/887745473883017246/887747134428946522',
    #             '力学のゼミ(講義) \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/888714546116698172/888714793261875221',
    #             '百人一首 \nチャンネルはこちら→ https://discord.com/channels/762884002591801344/890954837682966599/890956301482459207'
    #             'Notionを見てみよう！ \nhttps://receptive-tugboat-d9a.notion.site/c65da6964bb544c6bae61c4c4cce2174'
    #             ]

    if Flag == 1:
        keyword = message.content
        # if message.channel.id != channel_id:
        #    print("失敗")
        # else:
        print(keyword)
        Flag = 0
        check = 0
        for i in range(len(key_list)):
            if keyword in key_list[i]:
                await message.channel.send(semi_list[i])
            else: 
                check += 1
        if check == len(key_list):
            await message.channel.send('(^・ω・^)ノ そんなゼミはないなあ...。\n他のキーワードで調べるか、自分でゼミを作ろう！！')
    
    if message.content == 'ゼミ検索':
        # channel_id = message.channel.id
        Flag = 1
        await message.channel.send('(^・ω・^)ノ 調べたいゼミのキーワードを教えて！\nゼミの一覧が見たい時は、『一覧』、ゼミのカレンダーが見たい時は、『カレンダー』と書いてね')

    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        # 日本語で検索した上位2件を順番に表示
        for url in search(kensaku, lang="jp"):
            await message.channel.send(url)
            count += 1
            if(count == 2):
                break
    # google検索モードへの切り替え
    if message.content == '/google':
        ModeFlag = 1
        await message.channel.send('(^・ω・^)ノ こやーん(何を調べるの？)')

    list_1 = ['きつね', '狐', 'こやん', 'こやーん', 'くやーん','こゃーん']
    for list in list_1:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん")

    list_2 = ['お疲れ様です', 'おつかれさま', 'おつです', 'otudesu', ':Otsu_desu:', '落ちます']
    for list in list_2:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(おつかれさまです)")

    list_3 = ['うお', 'うおうお']
    for list in list_3:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(うおうお)")

    list_4 = ['すごい', 'sugoi', ':wakaru:', ':sugoi:', ':onaji:', ':wakarimi:', 'SUGOI']
    for list in list_4:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(わかる)")

    list_5 = ['こんばんは']
    for list in list_5:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(こんばんは)")

    list_6 = ['疲れた', 'つかれた']
    for list in list_6:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(がんばれ！！)")

    # list_7 = ['草', 'kusa']
    # for list in list_7:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん(草)")

    # list_8 = ['いい話', 'いいはなし', '良い話', '良いはなし']
    # for list in list_8:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん(いい話)")

    # list_9 = [':Alcoholism:', ':sake:', ':sakekasu:', ':beerOS1:', '酒', 'アルコール']
    # for list in list_9:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん(酒カス)")

    list_10 = [':usagi:', 'うさぎになりたい', 'うさぎ', 'ねこ', 'にゃん']
    for list in list_10:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(狐じゃい)")
    
    list_11 = [':mogu:', 'ご飯', 'ごはん', 'もぐもぐ', 'mogumogu']
    for list in list_11:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ むしゃむしゃ")

    # list_12 = [':apa:']
    # for list in list_12:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん(天晴れ！)")

    # list_13 = ['進捗どうですか']
    # for list in list_13:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send(" ```diff\n-(^・ω・^)時は来た！！！今こそ進捗を生むのだ....```")

    list_14 = ['こんにちは']
    for list in list_14:
        word = list in message.content
        if word is True:
            await message.channel.send("(^・ω・^)ノ こやーん(こんにちは)")

    # list_15 = [':kompeno:', 'こんぺの']
    # for list in list_15:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん(こんぺの〜)")

    list_16 = ['きつねうどん']
    for list in list_16:
        word = list in message.content
        if word is True:
            await message.channel.send("\n```diff\n-(^・ω・^)人間滅ぼすぞ...```")

    # list_17 = ['うまぴょい']
    # for list in list_17:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ \n俺のウララが！！\nずきゅんどきゅん走りだしー")

    # list_18 = [':yabaine:', 'やばいね']
    # for list in list_18:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん（これはやばいね）")

    # list_19 = ['サンタ', 'さんた', ':メリクリ:', 'クリスマス', ':santa:', ':christmas_tree:', 'Merry Christmas']
    # for list in list_19:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん（メリークリスマス！！）")

    # list_20 = ['あけおめ', 'あけましておめでとう']
    # for list in list_20:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん（明けましておめでとうございます！）")
    
    # list_21 = [':gift:', 'プレゼント', 'ぷれぜんと']
    # for list in list_21:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん（プレゼントは何を頼んだの？？）")

    # list_22 = ['煙突', 'えんとつ']
    # for list in list_22:
    #     word = list in message.content
    #     if word is True:
    #         await message.channel.send("(^・ω・^)ノ こやーん（うちには煙突はないので、テレポートを使って入ってきねて！！）")
   
    # /ch_create チャンネル名 というコマンドで反応する
    # /ch_createだけだと末尾の空白がDiscordの仕様により自動で削除されるため反応しない
    if message.content.startswith('/mkch '):
        # チャンネル名を取得
        ch_name = message.content.replace('/mkch ', '')

        # 権限を編集して作成するには以下のコードを追加
        permission = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=True),
            message.guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        # チャンネルを作成するカテゴリを取得
        category = message.guild.get_channel(802890832923459644)

        #取得したカテゴリに指定した名前でチャンネルを作成
        ch = await category.create_text_channel(name=ch_name, overwrites=permission)
        # 権限を編集して作成するには、上記で追加した permission を
        # overwrites に指定する

   
        await message.channel.send(f"{ch.mention} を作成しました。")

    # if message.content == '/embed':
    #     embed = discord.Embed( # Embedを定義する
    #                       title="Example Embed",# タイトル
    #                       color=0x00ff00, # フレーム色指定(今回は緑)
    #                       description="Example Embed for Advent Calendar", # Embedの説明文 必要に応じて
    #                       url="https://receptive-tugboat-d9a.notion.site/eb8d04db21dc4041bb0566ad232b4acf" # これを設定すると、タイトルが指定URLへのリンクになる
    #                       )
    #     embed.add_field(name="フィールド１",value="値１") # フィールドを追加。
    #     embed.add_field(name="フィールド２",value="値２")

    #     channel = client.get_channel(828147337523494943)

    #     await channel.send(embed=embed)

    if message.content == '/Twitter':
        await message.channel.send('(^・ω・^)ノ こやーん\nhttps://twitter.com/redgodcloudysky')

    if message.content == '/ホワイトボード':
        ModeFlag = 1
        await message.channel.send('(^・ω・^)ノ こやーん(https://r7.whiteboardfox.com)')

    if message.content == "/おみくじ":
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '中吉', '小吉', '吉', '凶', '大凶', '大吉', '中吉', '小吉', '吉', '凶', '大凶','大吉', '中吉', '小吉', '吉', '凶', '大凶','大吉', '中吉', '小吉', '吉','大大吉', '凶', '大凶','大吉', '中吉', '小吉', '吉', '凶', '大凶', '大大吉', '区', 'うな重', 'おみくじ', 'もう1回引けるドン', 'コ', '匚', '𠮷', '大𠮷', '羊吉🐏')), inline=False)
        embed.add_field(name="[今日のラッキーアイテム] ", value=random.choice(('お菓子', 'ハンカチ', 'ポケットティッシュ', '小説', 'ダンボール', '専門書', '専門書', 'うな重', 'きつねうどん', '自転車', 'スズメ', '光子')), inline=False)
        embed.add_field(name="[今日のキーワード]\n 気になったら調べてみよう！ ", value=random.choice(('車両運搬具減価償却累計額', 'クロスエントロピー', 'Höchst-Wacker process(ヘキストワッカー法) ', 'divD=ρ', 'ボース-アインシュタイン凝縮', 'ノーフリーランチ定理', 'Ramseyの定理', 'ディレトリトラバーサル', '表現型の可塑性', 'ロトカ・ヴォルテラの方程式', 'グラフェン', 'ニコルソン・ベイリーモデル', 'P=ρRT', 'シンプソンの多様度指数', 'クーパートリプル', 'ラジアルブリージングモード', 'ポテンシャル温度', '群書類従', 'リード＝シュテルンベルグ細胞', 'コードスイッチング', '双子語', '口笛言語', 'マカロネシア', 'ヒプナゴジア', 'Diels-Alder reaction', '頭内爆発音症候群', 'タキサン', '沸石', '月のナトリウム尾', 'x86_64', 'マクスウェル山', 'arm')), inline=False)
        #embed.add_field(name="[今日のラッキーアイテム] ", value=random.choice(('お菓子', 'ハンカチ', 'ポケットティッシュ', '小説', 'ダンボール', '専門書', '専門書', 'うな重', 'きつね')), inline=False)
        await message.channel.send(embed=embed)

    if message.content == "/プレゼント":
        embed = discord.Embed(title="きつねサンタさんからプレゼントが届いたよ！！", description=f"{message.author.mention}さんが貰えるプレゼントは...",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[プレゼント] ", value=random.choice(('専門書', '専門書', '専門書', '専門書', 'クッキー', '旅行券', '旅行券', '悪い子なのでサンタさんはきませんでした', 'ぬいぐるみ', 'ゲーム機', 'ハンカチ', 'ポケットティッシュ', '鰻重', 'きつねうどん', 'お菓子')), inline=False)
        #embed.add_field(name="[今日のラッキーアイテム] ", value=random.choice(('お菓子', 'ハンカチ', 'ポケットティッシュ', '小説', 'ダンボール', '専門書', '専門書', 'うな重', 'きつねうどん')), inline=False)
        #embed.add_field(name="[今日のラッキーアイテム] ", value=random.choice(('お菓子', 'ハンカチ', 'ポケットティッシュ', '小説', 'ダンボール', '専門書', '専門書', 'うな重', 'きつね')), inline=False)
        await message.channel.send(embed=embed)

    global q
    if message.author.bot:
        return
    elif message.content.startswith('qadd'):
        q.append(message.content[5:])
        await message.add_reaction('👍')
    elif message.content == 'qrand':
        if(len(q) == 0):
            await message.channel.send('問題がありません。')
        else:
            await message.channel.send(random.choice(q))
    elif message.content == 'qclear':
        q = []
        await message.channel.send('初期化しました。')
    elif message.content == 'qlist':
#discordは2000文字以上のメッセージを送れません。
        sub = 0
        while True:
            if sub + 1500 < len(str(q)):
                await message.channel.send('```py\n' + str(q)[sub:sub + 1500] + '```')
            elif sub < len(str(q)) - 8:
                await message.channel.send('```py\n' + str(q)[sub:] + '```')
            else:
                break
            sub += 1500
    elif message.content.startswith('qrem'):
        q.remove(message.content[5:])
        await message.add_reaction('👍')

    if message.content == "~join":
        #await message.channel.send("あ")
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("(^・ω・^)ノ こやーん（遊びにきたよ！）")

    elif message.content == "~leave":
        if message.guild.voice_client is None:
            await message.channel.send("(^・ω・^)ノ こやーん（どこにいるの？）")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("(^・ω・^)ノ こやーん（またね〜！）")


    if message.content == "/pomo":
        channel_name = message.channel.name
        pflag = True
        p_counter = 0
        print(str(channel_name))
        print(str(pflag))
        while pflag:
            p_counter += 1
            if p_counter % 4 == 0:
                rest_time = 900
            else:
                rest_time = 300
            await message.channel.send("(^・ω・^)ノ こやーん（ポモドーロ "+str(p_counter)+" 周目始めるよ！！）")
            
            print(str(p_counter))
            await asyncio.sleep(900)
            if pflag == False:
                break
            await message.channel.send("(^・ω・^)ノ こやーん（休憩時間）{}".format(message.author.mention))
            if p_counter % 4 == 0:
                await message.channel.send("今回は15分休憩だよ。おつかれさま。")
            await asyncio.sleep(rest_time)
            print(str(p_counter))
            
            # await message.channel.send("(^・ω・^)ノ こやーん（休憩時間終了！）")
        # ポモドーロ終了処理
        if pflag == False:
            await message.channel.send("(^・ω・^)ノ こやーん（お疲れ様でした！）\n 今回は "+str(p_counter)+"周やりました！")
            print(str(pf))
            p_counter += 1
    # ポモドーロ終了フラグ
    if message.content == "/pstop":
        pflag = False
        print(str(pflag))
        
    
    # if message.channel.name != akagami:
    #     print()
    # else:
        # while pf != 0:
        #     await message.channel.send("(^・ω・^)ノ こやーん（ポモドロー "+str(pf)+" 周目始めるよ！！）")
        #     pf += 1 
        #     print(str(pf))
        #     await asyncio.sleep(20)
        #     await message.channel.send("(^・ω・^)ノ こやーん（休憩時間）")
        #     await asyncio.sleep(10)
        #     print(str(pf))
        
        #     # await message.channel.send("(^・ω・^)ノ こやーん（休憩時間終了！）")
            
        #     if pf == 0:
        #         await message.channel.send("(^・ω・^)ノ こやーん（お疲れ様でした！）\n 今回は "+str(count)+"周やりました！")
        #         print(str(pf))
        #         break
                        
        #     count += 1   
    

    # while pf != 0:
    #     await message.channel.send("(^・ω・^)ノ こやーん（ポモドロー "+str(pf)+" 周目始めるよ！！）")
    #     pf += 1 
    #     print(str(pf))
    #     await asyncio.sleep(20)
    #     await message.channel.send("(^・ω・^)ノ こやーん（休憩時間）")
    #     await asyncio.sleep(10)
    #     print(str(pf))
        
    #     # await message.channel.send("(^・ω・^)ノ こやーん（休憩時間終了！）")
            
    #     if pf == 0:
    #         await message.channel.send("(^・ω・^)ノ こやーん（お疲れ様でした！）\n 今回は "+str(count)+"周やりました！")
    #         print(str(pf))
    #         break
                        
    #     count += 1   
    
    

    # if message.content.startswith('!trans'):
    #     say = message.content
    #     say = say[7:]
    #     if say.find('-') == -1:
    #         str = say
    #         detact = translator.detect(str)
    #         befor = detact.lang
    #         if befor == 'ja':
    #             convert_string = translator.translate(str, src=befor, dest='en')
    #             embed = discord.Embed(title='result', color=0xFFFFFF)
    #             embed.add_field(name='Befor', value=str)
    #             embed.add_field(name='After', value=convert_string.text, inline=False)
    #             await message.channel.send(embed=embed)
    #         else:
    #             convert_string = translator.translate(str, src=befor, dest='ja')
    #             embed = discord.Embed(title='result', color=0xFFFFFF)
    #             embed.add_field(name='Befor', value=str)
    #             embed.add_field(name='After', value=convert_string.text, inline=False)
    #             await message.channel.send(embed=embed)
    #     else:
    #         trans, str = list(say.split('='))
    #         befor, after = list(trans.split('-'))
    #         convert_string = translator.translate(str, src=befor, dest=after)
    #         embed = discord.Embed(title='result', color=0xFFFFFF)
    #         embed.add_field(name='Befor', value=str)
    #         embed.add_field(name='After', value=convert_string.text, inline=False)
    #         await message.channel.send(embed=embed)

    # if message.content.startswith('!trans'):
    #     say = message.content
    #     s = say[8:]
    #     detect = translator.detect(s)
    #     m = 'この文字列の言語は ' + detect.lang + ' です。'
    #     await message.channel.send(m)

    # if PFlag == 1:
    #     q = message.content
    #     PFlag = 0
        
    #     PrimTest = ''

    #     if q == 2:
    #         PrimTest = str(q) + 'は素数です！:laughing:'
    #         await message.channel.send("(^・ω・^)ノ "+ PrimTest)

    #     if q < 2 or q & 1 == 0:
    #         PrimTest = str(q) + 'は素数じゃないです！:rage:'
    #         await message.channel.send("(^・ω・^)ノ "+ PrimTest)
        
    #     d = (q - 1) >> 1
    #     while d & 1 == 0:
    #         d >>= 1

    #     for i in range(k):
    #         a = random.randint(1, q-1)
    #         t = d
    #         y = pow(a, t, q)
    #         while t != q-1 and y != 1 and y != q-1:
    #             y = pow(y, 2, q)
    #             t <<= 1
    #         if y != q-1 and t & 1 == 0:
    #             PrimTest = str(q) + 'は素数です！:laughing:'
    #         PrimTest = str(q) + 'は素数です！:laughing:'
    #     await message.channel.send("(^・ω・^)ノ "+ PrimTest)
    


    # # google検索モードへの切り替え
    # if message.content == '/素数':
    #     PFlag = 1
    #     await message.channel.send('(^・ω・^)ノ こやーん(僕が素数か判定してあげるよ)')

    # def hand_to_int(hand):
    #     """
    #     グー: 0, チョキ: 1, パー: 2 とする
    #     handはカタカナ，ひらがな表記，数字に対応する
    #     """
    #     hand_int = None
    #     if hand in ["グー", "ぐー", "0"]:
    #         hand_int = 0
    #     elif hand in ["チョキ", "ちょき", "1"]:
    #         hand_int = 1
    #     elif hand in ["パー", "ぱー", "2"]:
    #         hand_int = 2

    #     return hand_int

    # def get_player_result(player_hand, bot_hand):
    #     """
    #     勝利: 1, 敗北: 0, ひきわけ: 2 とする
    #     result_table[player_hand][bot_hand]で結果がわかるようにする
    #     """
    #     result_table = [
    #         [2, 1, 0],
    #         [0, 2, 1],
    #         [1, 0, 2]
    #     ]
    #     return result_table[player_hand][bot_hand]


    if message.channel.name == global_channel_name: #グローバルチャットにメッセージが来たとき
        #メッセージ受信部
        
        if message.author.bot: #BOTの場合は何もせず終了
            return
        #メッセージ送信部
        for channel in client.get_all_channels(): #BOTが所属する全てのチャンネルをループ
            
            if channel.name == global_channel_name: #グローバルチャット用のチャンネルが見つかったとき
                
                # if channel == message.channel: #発言したチャンネルには送らない
                #     continue

                embed=discord.Embed(description=message.content, color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
                embed.set_author(name=message.author.name,icon_url="https://media.discordapp.net/avatars/{}/{}.png?size=1024".format(message.author.id, message.author.avatar))
                embed.set_footer(text="{} / mID:{}".format(message.guild.name, message.id),icon_url="https://media.discordapp.net/icons/{}/{}.png?size=1024".format(message.guild.id, message.guild.icon))
                if message.attachments != []: #添付ファイルが存在するとき
                    embed.set_image(url=message.attachments[0].url)


                # name="{}#{}".format(message.author.name, message.author.discriminator) 
                # これでユーザータグを表示に変更できる


                await channel.send(embed=embed)
                await message.add_reaction('✅')

    # if message.channel.name == shintyoku:
        
    #     if message.author.bot: #BOTの場合は何もせず終了
    #         return
    #     for channel in client.get_all_channels(): #BOTが所属する全てのチャンネルをループ
            
    #         if channel.name == shintyoku:
    #             await message.add_reaction(':thumbsup:', ':sugoi:', ':apa:', ':iihanashi:')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '✅':
        if user.bot:
            return
        await reaction.message.delete()

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        send = [762887384584814642,\    # 雑談1
                837596936944746527,\    # 雑談2
                853666452636827658,\    # サ行通話
                828147337523494943,\    # タ行通話
                923918525997940746,\    # ナ行通話
                837571893900869642,\    # もくもく
                933379929079447582,\    # 英語縛り
                885417681145188362]     # 音楽室
        check = [840668644237377636,\   # 雑談1
                766918423292018728,\    # 雑談2
                835433259361763338,\    # サ行通話
                828147450502053958,\    # タ行通話
                923918594746748988,\    # ナ行通話
                933379789341986836,\    # もくもく
                885417227208249355,\    # 英語縛り
                837572272238755840]     # 音楽室
        n_embed = discord.Embed(title="音量調節は済みましたか？",
                                description="音楽botなどのデフォルト音声は非常に大きいです！通話に参加しているメンバーを右クリックすることで音量調節画面が開きます！(このメッセージは一分後自動的に削除されます)",
                                color=0xff0000)
        if after.channel is not None and after.channel.id == check[0]:
            n_channel = client.get_channel(send[0])
            d_embed = await n_channel.send(embed=n_embed)
            await d_embed.add_reaction('✅')
            await asyncio.sleep(10)
            await d_embed.delete()

# #@bot.command()
#     if message.content == '/じゃんけん':
#         hand_emoji_list = [":fist:", ":v:", ":hand_splayed:"]

#         player_hand = hand_to_int(hand)
#         if player_hand is None:
#             await ctx.send("不正な手です！もう一度やり直してください！！")
#             return

#         bot_hand = random(0, 2)

#         await ctx.send(
#             f"あなた: {hand_emoji_list[player_hand]}\n"
#             f"Bot: {hand_emoji_list[bot_hand]}"
#         )

#         result = get_player_result(player_hand, bot_hand)
#         if result == 0:
#             await ctx.send("残念，あなたの負けです！！")
#         elif result == 1:
#             await ctx.send("おめでとうございます！！，あなたの勝ちです:tada:")
#         else:
#             await ctx.send("あいこ！")


# @tasks.loop(seconds=60)
# async def loop():
#     # 現在の時刻
#     now = datetime.now().strftime('%H:%M')
#     if now == '12:00':
#         channel = client.get_channel(840116217250578442)
#         await channel.send('(^・ω・^)ノこやーん（12時だよ！）')  
#     elif now == '15:00':
#         channel = client.get_channel(840116217250578442)
#         await channel.send('(^・ω・^)ノこやーん（おやつの時間だよ！）')
#     elif now == '03:34':
#         channel = client.get_channel(840116217250578442)
#         await channel.send('(^・ω・^)ノこやーん（334!）')
    
#ループ処理実行
# loop.start()    


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
