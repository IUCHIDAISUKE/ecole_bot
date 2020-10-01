from discord.ext import commands
import discord
import random
import os
"""
Rule

機能ごとでmoduleを分けること
ここには、messageを送る以外のことは基本書かないようにすること！(バグチェックが容易になるはず)

To-do
1. 基本的な要素ごとでmodukeにわける
2. データ分析platform作成
3. DBとの連携、修正
4. reaction stampでの挙動の判定(つまり追加、するしないとか)
5. helpページの追加

基本的に、マジックコマンドとしてdiscord上から操作が完結できるようにする。
つまり、DBへの追加、修正はすべてbotとの会話で完結できるようにする。
マジックコマンドかつ管理者以外は反応しないような設計にする。

"""


# TOKEN = os.environ['DISCORD_BOT_TOKEN']
# DATABASE_URL = os.environ['DATABASE_URL']　

TOKEN = "NzU5NjgwMTQ0NTIwMTE4Mjkz.X3BBRA.kiqE6Pq_qRx09FvysztrBuuXyKM"
CHANNEL_ID = 761162241877475339  # 任意のチャンネルID(int)
GREET_TEXT = "Hello there!"  # これは外部でtextとして保存する


bot = commands.Bot(command_prefix='$')


client = discord.Client()
# member = client.Member()  # 　うまくいかない、API読むしか..........


def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members,
        '/roles': message.guild.roles,
        '/text_channels': message.guild.text_channels,
        '/voice_channels': message.guild.voice_channels,
        '/category_channels': message.guild.categories,
    }
    return data_table.get(command, '無効なコマンドです')


async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(GREET_TEXT)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await greet()


@client.event
async def on_disconnect():
    print('Logged in as')
    await greet()


# @bot.command()
# async def test(ctx, arg):
#     print(arg)
#     # if arg == "🥺":
#     await ctx.send(arg)

@client.event
async def on_message(message):
    # print(get_data(message))
    print(message.guild.text_channels)
    print(message.author)
    print(message.content)
    # print(message.member.activities)
    if "🥺" in message.content:
        print(message.content)
#         print(message.author)
        if client.user != message.author:
            message.channel.id = CHANNEL_ID

            embed = discord.Embed(
                title="Hi!!", description="How are you?", color=0xffcc33)
            await message.channel.send(embed=embed)
            # await message.channel.send("GOOD")

client.run(TOKEN)
