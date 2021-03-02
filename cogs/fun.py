import discord
import random
from discord.ext import commands


class fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot

    #Q&A

    @commands.command()
    async def qna(self, ctx, *, question):
        response = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
                    ]
        embed = discord.Embed(
                title="Q&A",
                description=f"Question: {question}\nAnswer: {random.choice(response)}"
                )
        embed.add_field(name="ㅤ",value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot),<:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)")
        await ctx.send(embed=embed)

    #F

    @commands.command()
    async def f(self, ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{ctx.author.mention} has paid the respect")
        else:
            embed = discord.Embed(
                    title="F",
                    description=
                    f"{ctx.author.mention} has paid the respect for {user.mention}"
                    )
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
    print("Fun file is loaded!")
