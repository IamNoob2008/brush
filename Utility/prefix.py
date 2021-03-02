import discord
import json
from discord.ext import commands

class prefix(commands.Cog, name="Settings"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, *, prefix):

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f"'{prefix}' is the new server prefix!")

def setup(bot):
    bot.add_cog(prefix(bot))
    print("prefix file is loaded!")
		