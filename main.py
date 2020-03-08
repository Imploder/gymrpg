import os
from dotenv import load_dotenv
from discord.ext import commands
from pymongo import MongoClient

from commands.hello import Hello
from commands.code import Code
from models.exercises import Exercises
from models.users import Users

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MONGO_URL = os.getenv('HEROKU_MONGNO_URI')
client = MongoClient(MONGO_URL)
db_connection = client.heroku_2g8whrvz

bot = commands.Bot(command_prefix='!')
# Update the database flag
INSERT_DB = False


@bot.event
async def on_ready():
    """Executes when the bot is ready to receive commands"""
    print(f"{bot.user.name} is ready to receive commands")


@bot.event
async def on_member_join(member):
    print("Someone Joined!")
    user_impl = Users(db_connection)
    user_impl.insert_user(member)


@bot.command(name="hello", help='Says hello!')
async def hello(ctx: commands.Context):
    """Executes on the !hello command"""
    await ctx.send(Hello.hello_there())


@bot.command(name="code", help='Provides the github link to the source code')
async def code(ctx: commands.Context):
    """Executes on the !code command"""
    await ctx.send(Code.code())


@bot.command(name="exercises", help="Lists all exercises")
async def exercises(ctx: commands.Context, search_term=None):
    """
    Executes on the !exercises command
    :param search_term: either a point value or exercise name to search for in the database
    """
    exercise_impl = Exercises(db_connection)

    if INSERT_DB:
        exercise_impl.insert_exercises()

    if search_term is None:
        await ctx.send(exercise_impl.get_exercises())

    if search_term is not None:
        await ctx.send(exercise_impl.query_exercises(search_term))


@bot.command(name="stats", help="Displays your stats")
async def stats(ctx: commands.Context):
    """Gets the current user's stats"""
    user_impl = Users(db_connection)
    await ctx.send(user_impl.get_users(ctx.author))


bot.run(TOKEN)
