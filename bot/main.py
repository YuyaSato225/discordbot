from discord.ext import commands
from discord import Intents, app_commands
import discord
import asyncio
from . import config
from .application.command import CommandCog
from .dependency import dependency
from .Usecases.ChatGPTUsecase import ChatGPTUsecase


async def main():
    # Botを定義
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="/",intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is ready")
        #await bot.tree.sync()
    gpt = injector.resolve(ChatGPTUsecase)
    # Cogを有効化
    await bot.add_cog(CommandCog(bot, gpt))
    # Botを起動
    await bot.start(config.DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    injector = dependency()
    asyncio.run(main())
