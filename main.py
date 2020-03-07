import os
from dotenv import load_dotenv
from discord.ext import commands
from pymongo import MongoClient

from commands.hello import Hello
from models.exercises import Exercises

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MONGO_URL = os.getenv('MONGODB_URL')
client = MongoClient(MONGO_URL)

bot = commands.Bot(command_prefix='!')
INSERT_DB = False


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to receive commands")


@bot.command(name="hello", help='Says hello!')
async def display_stats(ctx: commands.Context):
    await ctx.send(Hello.hello_there())


@bot.command(name="exercises", help="Lists all exercises")
async def display_exercises(ctx: commands.Context, arg=None):
    exercises = Exercises(client)

    if INSERT_DB:
        exercises.insert_exercises()

    if arg is None:
        await ctx.send(exercises.get_exercises())

    if arg is not None:
        await ctx.send(exercises.query_exercises(arg))



bot.run(TOKEN)
