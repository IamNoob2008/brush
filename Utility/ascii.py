import discord
import pyfiglet
from discord.ext import commands

class ascii(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ascii(self, ctx, *, text):
        a = pyfiglet.figlet_format(text)
        await ctx.send(a)

def setup(bot):
    bot.add_cog(ascii(bot))
    print("ascii file is loaded!")
