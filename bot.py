from config import BOT
import discord
import discord.ext
from discord.ext import commands
from discord.utils import get
import time
import random
import requests


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
async def on_message(ctx):
	blacklist = [" x", "ily", "xxx"]
	if ctx.author.id == 815009535063621634:
		for x in blacklist:
			if x in ctx.content:
				await ctx.channel.purge(limit=1)
				for i in range(1, 5):
					await ctx.channel.send("FUCK BOY ALERT")
	await bot.process_commands(ctx)
#	mentionL = ["<@!530571508482048511>", "<@!396025519398977548>", "<@!784910255427289118>"]
#	if ctx.author.id == 518241202886410261:
#		for x in mentionL:
#			if x in ctx.content:
#				print("worked")
#				for y in range(1, 69):
#					await ctx.author.send("LMAO UR BAD KID")

                    
@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Member')
    await member.add_roles(role)

@bot.command()
async def cool(ctx):
    user = ctx.guild.get_member(530571508482048011)
    await ctx.channel.send(f"{user.mention}")
    print("Ran successfully!")
    

@bot.command()
async def kawaii(ctx):
#    kpics = ['02.gif', 'neko.gif', 'panda.gif', '02-2.gif', 'smolcat.png']
#    await ctx.channel.send(file=discord.File('pics/' + random.choice(kpics)))
	tmp = []
	res = requests.get("https://g.tenor.com/v1/search?key=9474HZRJCXNR&q=anime_girl_kawaii&locale=en_US&contentfilter=medium&limit=50").json()
	for count, x in enumerate(res['results']):
		gif = res['results'][count]['media'][0]['tinygif']['url']
		tmp.append(gif)
	#print(tmp)
	await ctx.channel.send(random.choice(tmp))
        
        
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
        await ctx.channel.purge(limit=1)
        
        
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
async def hawaii(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(file=discord.File('pics/hawaii.jpeg'))


@bot.command()
async def mute(ctx, user: discord.Member):
    role = get(ctx.guild.roles, name='Member')
    await user.add_roles(member, role)




# Hey!

print("Startup successful!")

bot.run(token)
