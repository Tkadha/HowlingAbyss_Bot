import random

import discord
from discord.ext import commands
import howlingabyss
import overwatch

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!명령어"))
    print("봇이 시작되었습니다.")

@bot.command()
async def 명령어(ctx):
    await ctx.send('!업데이트: 가장 최신에 업데이트된 정보와 날짜를 알립니다.')
    await ctx.send('!칼바람 (num): 각 팀에게 num개의 챔피언을 랜덤하게 뽑습니다.')
    await ctx.send('!오버워치: 오버워치 맵 중 랜덤으로 하나 선택합니다.(특정 맵 제외)')
    await ctx.send('!오버워치목록: 오버워치 맵들을 표시합니다.(특정 맵 제외)')
    await ctx.send('!팀섞기: 현재 음성 채널에 인원으로 2개의 팀을 만듭니다.')
    await ctx.send('!진영 이름1 이름2: 레드와 블루진영을 선정합니다.')
    await ctx.send('!공수 이름1 이름2: 공수와 맵 선택권을 선정합니다.')
    await ctx.send('!종료: 종료합니다.')
    await ctx.send('추후 추가될 수 있습니다.')

@bot.command()
async def 업데이트(ctx):
    await ctx.send('2024.08.04 공수 추가')
    await ctx.send('2025.01.17 암베사 추가 업데이트')
    await ctx.send('2025.02.05 멜 추가')

@bot.command()
async def 칼바람(ctx, number: int):
    sl = howlingabyss.sample(number)
    red_list = sl[:number]
    blue_list = sl[number:]
    red_list_str = ', '.join(red_list)
    blue_list_str = ', '.join(blue_list)
    await ctx.send('1팀\n||'+red_list_str+'||')
    await ctx.send('2팀\n||'+blue_list_str+'||')

@bot.command()
async def 오버워치(ctx):
    sl = overwatch.sample()
    await ctx.send(sl[0])

@bot.command()
async def 오버워치목록(ctx):
    sl = overwatch.alllist()
    sl_str = ', '.join(sl)
    await ctx.send(sl_str)

@bot.command()
async def 팀섞기(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        members = voice_channel.members

        mem_list = [member.display_name for member in members]
        random.shuffle(mem_list)
        mid = len(mem_list)//2
        team1 = mem_list[:mid]
        team2 = mem_list[mid:]
        await ctx.send('블루(1팀):'+', '.join(team1))
        await ctx.send('레드(2팀):'+', '.join(team2))
    else:
        await ctx.send('음성 채널에 접속하고 있지 않습니다.')

@bot.command()
async def 진영(ctx, *names):
    name_list = list(names)
    random.shuffle(name_list)
    await ctx.send('블루(1팀) - '+name_list[0]+'\n')
    await ctx.send('레드(2팀) - '+name_list[1])

@bot.command()
async def 공수(ctx, *names):
    name_list = list(names)
    random.shuffle(name_list)
    await ctx.send('공수 - ' + name_list[0] + '\n')
    await ctx.send('맵 - ' + name_list[1])

@bot.command()
async def 종료(ctx):
    await ctx.send("칼바람 봇을 종료합니다.")
    await bot.close()

# 개인 디스코드 api 보안을 위해 실제 동작은 보안키를 작성하여 실행합니다.
bot.run('api 보안키')