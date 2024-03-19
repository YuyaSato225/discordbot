import discord
from discord.ext import commands
from bot.application import config
from bot.application import utils

# Botの接続と動作設定
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def test(ctx):
    await ctx.send('おはよう')

# Botのトークンを設定
bot.run(config.DISCORD_BOT_TOKEN)

