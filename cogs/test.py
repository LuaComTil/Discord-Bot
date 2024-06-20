import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ta on papai")

    @commands.command()
    async def ping(self, ctx):
        ping_embed = discord.Embed(
            title="Ping",
            description="bot/ms",
            color=discord.Color.blue()
        )

        latency_ms = round(self.bot.latency * 1000)
        ping_embed.add_field(
            name=f"{self.bot.user.name} tá lagado em:",
            value=f"{latency_ms} ms seh loko",
            inline=False
        )

        ping_embed.set_footer(
            text=f"Pedido pelo curioso {ctx.author.name}",
            icon_url=ctx.author.avatar.url
        )

        await ctx.send(embed=ping_embed)

async def setup(bot):
    await bot.add_cog(Test(bot))
    print(f"Cog {__name__} got loaded")
