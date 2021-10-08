import discord
import json
import os
from discord import message
from discord.client import _ClientEventTask
from discord.ext import commands

def get_prefix(client, message):
      with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
      
           
      return prefixes[str(message.guild.id)] 

client = commands.Bot (command_prefix = get_prefix)


@client.event
async def on_ready():
      print('Went online!')

@client.event
async def on_guild_join(guild):
      with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes[str(message.guild.id)] = '.'

      with open('prefixes.json', 'w') as f:
       json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
      with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes.pop(str(guild.id))

      with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

@client.command()
async def changeonprefix(ctx, prefix):
      with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)  

      await ctx.send(f'Prefix changed to: {prefix}')

@client.event
async def on_command_error(ctx, error):
 if isinstance (error, commands.CommandNotFound):     
      await ctx.send('Invaid Command type .help to see command description')

      
@client.command()
async def load(ctx, extension):
      client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
      client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
      client.unload_extension(f'cogs.{extension}')    
      client.load_extension(f'cogs.{extension}')  

for filename in ('./cogs'):
      if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}') 


client = commands.Bot (command_prefix = '.')

@client.event
async def on_ready():
      print('Went online!')

@client.event
async def on_command_error(ctx, error):
 if isinstance (error, commands.CommandNotFound):     
      await ctx.send('Invaid Command type .help to see command description')

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
      
@client.command()
async def load(ctx, extension):
      client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
      client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
      client.unload_extension(f'cogs.{extension}')    
      client.load_extension(f'cogs.{extension}')  

for filename in ('./cogs'):
      if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}') 


client.run('ODk1MzQyOTYwODMxNTI0ODY0.YV3LHA.NPcehQ4dV0Y9YUEaVpBvZDAof0k')
