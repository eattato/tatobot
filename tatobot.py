import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)

workChannel = None

@client.event
async def on_ready():
    print("로드 성공")

@client.event
async def on_message(msgContent):
    global workChannel
    guild = msgContent.guild
    if workChannel == None:
        if msgContent.content == ".setchan":
            if msgContent.author == guild.owner:
                workChannel = msgContent.channel
                await msgContent.channel.send("봇 채널을 변경했습니다 - 채널 이름 : {}".format(msgContent.channel.name))
    else:
        if msgContent.content == ".setchan":
           if msgContent.author == guild.owner:
                workChannel = msgContent.channel
                await msgContent.channel.send("봇 채널을 변경했습니다 - 채널 이름 : {}".format(msgContent.channel.name))

        if msgContent.channel == workChannel:
            if msgContent.author.bot:
                return None
            
            if msgContent.content == ".cntest":
                await msgContent.channel.send("테스트 성공")

            elif msgContent.content == ".dmtest":
                await msgContent.author.send("테스트 성공")

            elif msgContent.content == ".reptest":
                await msgContent.reply("{} 에게 답장함".format(msgContent.author.mention))

            elif msgContent.content.startswith(".spam"):
                targetlist = msgContent.content.split(' ')
                if len(targetlist) == 1 or len(targetlist) == 0:
                    await msgContent.reply("대상 지정 실패")
                else:
                    del targetlist[0]
                    target = ""
                    for ind in targetlist:
                        if ind == targetlist[0]:
                            target = target + ind
                        else:
                            target = target + " " + ind
                
                    realtarget = None
                    for user in guild.members:
                        if realtarget == None:
                            if user.name == target:
                                realtarget = user
                            else:
                                await msgContent.reply("{} 는 타겟 {} 와 맞지 않음".format(user.name, target))



                    if realtarget != None:
                        await msgContent.reply("대상 : {}".format(realtarget.name))
                        for count in range(30):
                            await msgContent.channel.send("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention, realtarget.mention))

                    else:
                        await msgContent.reply("대상 발견 실패")
                    
            elif msgContent.content.startswith(".erase"):
                cleancountarr = msgContent.content.split(' ')
                if len(cleancountarr) > 1:
                    cleancount = int(cleancountarr[1])
                    if cleancount > 0:
                        await msgContent.delete()
                        await msgContent.channel.purge(limit = cleancount)
                        await msgContent.channel.send("총 {} 개의 메세지를 삭제했습니다.".format(cleancount))
                    else:
                        await msgContent.reply("{} 매개 변수는 0 이상 이여야합니다!".format(msgContent.author.mention))
                    
                else:
                    await msgContent.reply("{} 매개 변수가 없습니다!".format(msgContent.author.mention))






access_token = os.environ['BOT_TOKEN']
client.run(access_token) 
