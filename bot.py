from config import BOT
import discord
import discord.ext
from discord.ext import commands
from discord.utils import get
import time
import random
import requests

intents = discord.Intents.all()
intents.members = True
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
				for i in range(0, 5):
					await ctx.channel.send("FUCK BOY ALERT")
	await bot.process_commands(ctx)
    
    ######################################################################################
    
	mentionL = ["<@!530571508482048511>", "<@!396025519398977548>", "<@!784910255427289118>"]
	if ctx.author.id == 251161801805266945:
		for x in mentionL:
			if x in ctx.content:
				print("worked")
				for y in range(1, 10):
					await ctx.author.send("Karma")

	if ctx.author.id == 530571508482048011 or 396025519398977548:
		triggers = ["hey baby", "hey bb"]
		for x in triggers:
			if x in ctx.content.lower():
				yikes = ["hey daddy ;\)", "come to my dmszzzz"]
				await ctx.channel.send(random.choice(yikes))

@bot.command()
async def test(ctx):
    print(ctx.fetch_roles())
                
                

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
	res = requests.get("https://g.tenor.com/v1/search?key=9474HZRJCXNR&q=anime_girl_kawaii&locale=en_US&contentfilter=low&limit=50").json()
	for count, x in enumerate(res['results']):
		gif = res['results'][count]['media'][0]['tinygif']['url']
		tmp.append(gif)
	#print(tmp)
	await ctx.channel.send(random.choice(tmp))

    
@bot.command()
async def loli(ctx):
	tmp2 = []
	res2 = requests.get("https://g.tenor.com/v1/search?key=9474HZRJCXNR&q=loli&locale=en_US&contentfilter=low&limit=50").json()
	for count, x in enumerate(res2['results']):
		gif2 = res2['results'][count]['media'][0]['tinygif']['url']
		tmp2.append(gif2)
	await ctx.channel.send(random.choice(tmp2))
 
  
        
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

        
        

bot.remove_command("purge")
@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount):
    try:
        await ctx.channel.purge(limit=int(amount))
        await ctx.author.send(f'Purge successful! You purged {amount} messages.')
    except:
        await ctx.channel.send("Not a valid argument!")
        
@pierre.error
async def pierre_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.purge(limit=1)

@bot.event
async def on_member_join(member):
    #Channel IDS
	MemChannelId = bot.get_channel(816361625253838888)
	BoostChannelId = bot.get_channel(816361946278395943)
	#EMOJIS
	print("\nMember joined!")
	await MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
	await BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
    ## AUTO ROLE ##
	print("\nAssigning role...")
	role = get(member.guild.roles, name='Member')
	await member.add_roles(role)
	print("Role assigned!\n")
    
    
@bot.event
async def on_member_remove(member):
    #Channel IDS
	MemChannelId = bot.get_channel(816361625253838888)
	BoostChannelId = bot.get_channel(816361946278395943)
	#EMOJIS
	await MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
	await BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
	print("\nMember left!")

    
    
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}   

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    if not voice.is_connected:
        await channel.connect()
    else:
        ctx.channekl.send("Already in a voice channel!")
        
    voice = get(bot.voice_clients)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

    voice.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
    voice.source = discord.PCMVolumeTransformer(voice_client.source, 1)
    voice.source = discord.PCMVolumeTransformer(voice.source)


    
    



# Hey!

print("Startup successful!")

bot.run(token)