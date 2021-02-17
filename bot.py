from config import BOT
import discord
import discord.ext
from discord.ext import commands
from discord.utils import get
import time
import random

intents = discord.Intents.all()
# initial_extensions = ['cogs.cogs']
token = BOT['TOKEN']
bot = commands.Bot(command_prefix=BOT['PREFIX'], intents=intents, help_command=None)


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)


# Rich Presence
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Truett65"))


@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Member')
    await member.add_roles(role)



@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kawaii(ctx):
    kpics = ['02.gif', 'neko.gif', 'panda.gif', 'shaq.jpeg', '02-2.gif', 'smolcat.png']
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(file=discord.File('pics/' + random.choice(kpics)))


@kawaii.error
async def kawaii_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.purge(limit=1)





@bot.command()
async def help(ctx):
    rembed = discord.Embed(title="I'm Super Truett!", color=0x3a88fe)
    rembed.add_field(name="I serve for Truett65's discord server", value="Contact admins for any other concerns", inline=False)
    rembed.set_footer(text="Bot made by 2SurvivalGuys")
    await ctx.channel.send(embed=rembed)
    time.sleep(0.5)
    await ctx.channel.send("**Also check the bots help page for all the commands!** https://github.com/leifadev/super-truett/wiki")


## VOICE STUFF

@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def calmdown(ctx):
    try:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        voice = get(bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio('sounds/calmdownjamal.wav'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 20.0
        time.sleep(4.5)
        await voice.disconnect()
    except:
        await ctx.author.send("You have to be in a voice channel to use this!")

@calmdown.error
async def calmdown_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.purge(limit=1)


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def pierre(ctx):
    try:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        voice = get(bot.voice_clients)
        voice.play(discord.FFmpegPCMAudio('sounds/pierre.wav'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 10.0
        time.sleep(4.5)
        await voice.disconnect()
    except:
        await ctx.author.send("You have to be in a voice channel to use this!")
        await ctx.channel.purge(limit=1)


@pierre.error
async def pierre_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.purge(limit=1)



@bot.command()
@commands.has_role("Admin")
async def purge(ctx, amount):
    try:
        await ctx.channel.purge(limit=int(amount))
    except:
        await ctx.channel.send("Please specify a valid number!")


@bot.command()
async def hawaii(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(file=discord.File('pics/hawaii.jpeg'))



## MORE TO ADD SINCE FEBURARY 17TH 2021
## MORE TO ADD SINCE FEBURARY 17TH 2021
## MORE TO ADD SINCE FEBURARY 17TH 2021



# Hey!

print("Startup successful!")

bot.run(token)