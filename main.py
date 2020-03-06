import os
from dotenv import load_dotenv
from discord.ext import commands

from commands.hello import Hello

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to receive commands")


@bot.command(name="hello")
async def display_stats(ctx: commands.Context):
    await ctx.send(Hello.hello_there())


bot.run(TOKEN)
