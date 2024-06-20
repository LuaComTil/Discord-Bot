import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle

bot =  commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot_status = cycle(["Fazendo um DELETE sem WHERE","Criando um ponteiro com endereço nulo","(WHILE = TRUE) { este bot não estará vendendo os dados deste servidor }"])

@tasks.loop(seconds=24)
async def changeStatus():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

@bot.event
async def on_ready():
    print("bot prontasso")
    changeStatus.start()

@bot.command()
async def oi(ctx):
    await ctx.send(f"Aoeba {ctx.author.mention} bão?")

with open("token.txt") as file:
    token = file.read().strip()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())
