import discord
from discord.ext import commands

class help(commands.Cog, name="Help"):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(color=0x00FF00)
		embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		embed.add_field(name="Full BOT Guide", value=f"[Help](https://rsgametech.gitbook.io/element/)", inline=False)
		embed.add_field(name="BOT Info", value=f"[Invite](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)", inline=False)
		try:
			await ctx.author.send(embed=embed)
			await ctx.send(f"{ctx.message.author}")
		except:
			await ctx.send()

def setup(bot):
	bot.add_cog(help(bot))
	print("help file is loaded!")
