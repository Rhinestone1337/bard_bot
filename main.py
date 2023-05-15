import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from bardapi import Bard

load_dotenv()
BARD_API_KEY = os.getenv("BARD_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
os.environ['_BARD_API_KEY'] = BARD_API_KEY


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def bard(ctx, *,  arg):
    ans = Bard().get_answer(arg)['content']
    await ctx.send(ans)


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
