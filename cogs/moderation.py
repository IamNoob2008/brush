import discord
from discord.ext import commands

class moderation(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    #Kick

    @commands.command(brief="This command is used to kick the members from the current server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      """kicks mentioned user
      parameters
        • user
          mention the user to kick
      """
      await member.kick(reason=reason)
      await ctx.channel.purge(limit=1)
      embed = discord.Embed(
            title="Kick News",
            description=f"{member.name} has successfully kicked for {reason}",
            color=discord.Color.red()
            )
      embed.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
      await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Please mention the Name```")
      elif isinstance(error, commands.MemberNotFound):
          await ctx.send("```Member not found in this server```")
      elif isinstance(error, commands.MissingPermissions):
          KE = discord.Embed(
                title="Kick News",
                description=
                f"{ctx.author.mention}, you don't have the Kick Member permission!",
                color=0xFF0000)
          KE.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
          await ctx.send(embed=KE)

    #Ban

    @commands.command(brief="This command is used to ban the members from the current server.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="Ban News",
            description=f"{member.name} has successfully banned for {reason}",
            color=discord.Color.red()
            )
        embed.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("```Please mention the Name```")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("```Member not found in this server```")
        elif isinstance(error, commands.MissingPermissions):
            BE = discord.Embed(
                title="Ban News",
                description=f"{ctx.author.mention}, you don't have the Ban Member permission!",
                color=0xFF0000)
            BE.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
            await ctx.send(embed=BE)

    #Clear

    @commands.command(description="This command is used to clear the number of message from the current channel.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        embed = discord.Embed(
            title="Clear News",
            description="Message has been succesfully clear",
            color=0xE67E22
        )
        embed.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            EN = discord.Embed(description=f"{ctx.author.mention}, you have to  specify the amount of message to delete.")
            EN.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
            await ctx.send(embed=EN)
        elif isinstance(error, commands.MissingPermissions):
            EP = discord.Embed(description=f"{ctx.author.mention}, you don't have the 'Manage Message' permision to use this command.")
            EP.add_field(name="Links", value=f"<:DiscordBOT:801303572183777280>: [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot) | <:supporter:775594205186883585>: [Support Server](https://discord.gg/PKP4mG6E3G)", inline=False)
            await ctx.send(embed=EP)

    #Embed

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title: str = None,*, description: str = None):
        embed = discord.Embed(title=f"{title}",
                            description=f"{description}",
                            color=0xFFFF00
                            )
        await ctx.send(embed=embed)

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("```You don't have permision to do this```")

def setup(bot):
    bot.add_cog(moderation(bot))
    print("Moderation file is loaded!")
