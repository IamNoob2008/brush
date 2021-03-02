import discord
import asyncio
from discord.ext import commands

class util(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    #User Avatar

    @commands.command()
    async def user_av(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed()
        embed.add_field(name=user.name,value=f"[Download]({user.avatar_url})")
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Server Avatar

    @commands.command()
    async def server_av(self, ctx):
        embed = discord.Embed()
        embed.add_field(name=ctx.guild.name,value=f"[Download]({ctx.guild.icon_url})")
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Ping

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send("Pinging <a:WindowsDotLoading:809471466311516211>")
        await ctx.send(msg)
        await asyncio.sleep(5)
        embed = discord.Embed(title="Pong!",description=f"Your latency is {round(self.bot.latency * 1000)}ms",color=0x00FF00)
        embed.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
        await msg.edit(content = "",embed=embed)

def setup(bot):
    bot.add_cog(util(bot))
    print("Utility file is loaded!")
