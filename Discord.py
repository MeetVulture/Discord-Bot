import discord
from discord.ext import commands

client = commands.Bot (command_prefix = '.')

@client.event
async def on_ready():
      print('Went online!')


@client.command()
async def clear(ctx, amount=6):
      await ctx.channel.purge(limit=amount) 

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

@client.command()
async def hi(ctx):
      await ctx.send(f'Hi!,how are you?')
      await ctx.send(f'My name is G0_BOT')
      await ctx.send(f'What is your name?')

@client.command()
async def lol(ctx):
      await ctx.send(f' hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahhahahahahah!')

@client.command()
async def angry(ctx):
      await ctx.send(f'chill down...!!')

@client.command()
async def happy(ctx):
      await ctx.send(f'Hey! , i am happy too!!')
      await ctx.send(f'be happy forever!!!!!!!!')

@client.command()
async def everyone(ctx):
      await ctx.send(f'@everyone pls reply!')
      
@client.command()
async def here(ctx):
      await ctx.send(f'@here pls reply! ')

@client.command()
async def howto(ctx):
      await ctx.send(f'for dicord bot ask the user MʀGᴏᴋᴜʟBɪɢ#9503')
      await ctx.send(f'you just ask and tell, what name do you want for your bot and persnolisations!')
      await ctx.send(f'after some time you will have a bot!!!')

@client.command()
async def sad(ctx):
      await ctx.send(f'dont worry!, be happy!')
      await ctx.send(f'make sure you breath in and breath out')
      await ctx.send(f'and erase the bad momories')


@client.command()
async def name(ctx):
      await ctx.send(f'my name is G0_BOT and made by MʀGᴏᴋᴜʟBɪɢ#9503')


@client.command()
async def spam(ctx):
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      await ctx.send(f' @here @everyone oifdsjdoifjoidsanfoisafoisafoinvafoisjdjdfpijofdsjosjfoisjfiuhfouhfoiusahfoiushiuehfiudhfewhfiuafiudsajfdsiujfidsjfoisjojsafdijdfijfijidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfidjfijdifkjsafnsaiudhfnoisauhdABDWNINIVSNIDSJNNCISNICNKmkIKOjKKIO092I9I0938320949840924020923-21VSS')
      


client.run('give ur token here')
