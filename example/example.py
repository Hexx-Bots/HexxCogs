from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def example_command(self, ctx: commands.Context) -> None:
        await ctx.send("Success!")


def setup(bot):
    bot.add_cog(Example(bot))
