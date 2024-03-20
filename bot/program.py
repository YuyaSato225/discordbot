from discord.ext import commands
from discord import Intents, app_commands
import discord
import asyncio
from . import config
from .application.command import CommandCog

async def main():
    # Botを定義
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="/",intents=intents)

    # on_readyの前に実行されるイベントリスナー
    @bot.event
    async def setup_hook() -> None:
        guild_ids = [626717930591354881] # すぐに同期したいサーバーのIDを入れる
        for g in guild_ids:
            try:
                await bot.tree.sync(guild=discord.Object(id=g))
                print(f"{g}との同期が完了しました")
            except discord.errors.Forbidden:
                # やりすぎるとForbiddenになるので、一応例外処理を入れておく
                print(f"サーバーID:{g}に登録できませんでした。")

    # Cogを有効化
    await bot.add_cog(CommandCog(bot))
    # Botを起動
    await bot.start(config.DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
