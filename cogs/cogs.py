from discord.ext import commands
<<<<<<< Updated upstream
from ruamel import yaml
=======

>>>>>>> Stashed changes
bot = commands.Bot



<<<<<<< Updated upstream
=======
class GeneralCogs(commands.Cog):
    def __init__(self, bot):from discord.ext import commands

bot = commands.Bot


>>>>>>> Stashed changes

class GeneralCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
<<<<<<< Updated upstream
		self.BoostChannelId = int
		self.MemChannelId = int

        self.payload = [
            {
                'Options': {
                    'memCount': self.MemChannelId,
                    'boostCount': self.BoostChannelId
                }
            }
        ]
        
        # Server member and boosts listener

        @commands.command()
		@commands.has_permissions(administrator=True)
		async def assignboost(ctx, bChannel):
        	bCh
        	with open
        
        @commands.Cog.listener()
        async def on_member_join(member):
            #Channel IDS
            MemChannelId = bot.get_channel(816361625253838888)
            BoostChannelId = bot.get_channel(816361946278395943)
            #EMOJIS
            print("\nMember joined! \nSadly, we don't have the objects to identify that member.\n")
            await MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
            await BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
            ## AUTO ROLE ##
            print("\nAssigning role...")
            role = get(member.guild.roles, name='Member')
            await member.add_roles(role)
            print("Role assigned!\n")


        @commands.Cog.listener()
        async def on_member_remove(member):
            #Channel IDS
            MemChannelId = bot.get_channel(816361625253838888)
            BoostChannelId = bot.get_channel(816361946278395943)
            #EMOJIS
            await MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
            await BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
            print("\nMember left!\nSadly, we don't have the objects to identify that member.\n")
            
            
            
=======
        self.memberCount = None
        self.boostsCount = None


        # Server member and boosts listener

        @commands.Cog.listener()
        async def on_ready(self, ctx):
            memChannel = bot.get_channel(816361625253838888)
            # boostChannel = bot.get_channel(816361946278395943)
            await bot.VoiceChannel.edit(channel=memChannel, name="Test")
        self.bot = bot
        self.memberCount = None
        self.boostsCount = None


        # Server member and boosts listener

        @commands.Cog.listener()
        async def on_ready(self, ctx):
            memChannel = bot.get_channel(816361625253838888)
            # boostChannel = bot.get_channel(816361946278395943)
            await bot.VoiceChannel.edit(channel=memChannel, name="Test")
>>>>>>> Stashed changes
