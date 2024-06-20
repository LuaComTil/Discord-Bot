import discord
from discord.ext import commands

class Ping(commands.Cog):
#   Initialize bot as a attribute
    def __init__(self, bot):
        self.bot = bot

#   Warn when Cog is ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está pronto")

#Creates Embed as an OBJ
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
#       Send the Embed in the channel that was called
        await ctx.send(embed=ping_embed)

#Register Cog in the bot
async def setup(bot):
    await bot.add_cog(Ping(bot))
    print(f"{__name__} foi carregado")
