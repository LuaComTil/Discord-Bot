import discord
from discord.ext import commands
import os
import asyncio

bot =  commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot prontasso")

@bot.command()
async def on(ctx):
    await ctx.send(f"pai ta on!, {ctx.author.mention}!? ta moscando!")

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
