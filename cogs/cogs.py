from discord.ext import commands
from ruamel import yaml
import time
import datetime
bot = commands.Bot


class GeneralCogs(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.BoostChannelId = int
		self.MemChannelId = int
		self.creepmode = True
        
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
		async def togglecreep(self, ctx):
			if isinstance(ctx.channel, discord.channel.DMChannel):
				if self.creepmode:
					self.creepmode = False
				else:
					self.creepmode = True
				await ctx.author.send("creep mode enable XDD")
				time.sleep(1)
				await ctx.author.purge(limit=1)


		@commands.Cog.listener()
		async def on_ready(self, ctx):
			peeps = [802990337592131614, 774384309267464214, 722091734519119992]
			if ctx.author.id == 802990337592131614 or 774384309267464214 or 722091734519119992:
				if self.creepmode:
					for peep in peeps:
						await ctx.bot.get_user(peep).send("heyyyyyy")
    			
                
		@commands.Cog.listener()
		async def on_member_join(self,member):
            #Channel IDS
			self.MemChannelId = bot.get_channel(816361625253838888)
			self.BoostChannelId = bot.get_channel(816361946278395943)
            #EMOJIS
			print("\nMember joined! \nSadly, we don't have the objects to identify that member.\n")
			await self.MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
			await self.BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
            ## AUTO ROLE ##
			print("\nAssigning role...")
			role = get(member.guild.roles, name='Member')
			await member.add_roles(role)
			print("Role assigned!\n")


		@commands.Cog.listener()
		async def on_member_remove(member):
            #Channel IDS
			self.MemChannelId = bot.get_channel(816361625253838888)
			self.BoostChannelId = bot.get_channel(816361946278395943)
            #EMOJIS
			await self.MemChannelId.edit(name=f'\N{BAR CHART} Members: {member.guild.member_count}')
			await self.BoostChannelId.edit(name=f'\N{GEM STONE} Boosts: {member.guild.premium_subscription_count}')
			print("\nMember left!\nSadly, we don't have the objects to identify that member.\n")
            
            
            
