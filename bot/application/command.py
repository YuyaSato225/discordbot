import discord
from discord.ext import commands
from discord import app_commands
from ..Usecases.ChatGPTUsecase import ChatGPTUsecase
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse
from injector import inject

# スラッシュコマンドのCog
class CommandCog(commands.Cog):
    @inject
    def __init__(self, bot, gpt: ChatGPTUsecase):
        self.bot = bot
        self.gpt = gpt

    # 静的に決定されたメッセージを返すスラッシュコマンド
    @app_commands.command(name='test', description='あいさつをするよ')
    async def test(self, ctx: discord.Interaction):
        await ctx.response.send_message('おはようございます！')

    # ChatGPTと会話するためのスラッシュコマンド
    @app_commands.command(name='chat', description='ChatGPTと会話できます')
    @app_commands.describe(message_text='送信するメッセージ')
    async def chat(self, ctx: discord.Interaction, message_text: str):
        # 実際の返答を即座に行えないため、仮の返答をする
        await ctx.response.defer()
        # OpenAI apiにアクセスし、結果を得る
        response = self.gpt.send_request(ChatGPTRequest(message_text))
        await ctx.followup.send(f'ユーザー : {message_text}\n\nつくよみちゃん : {response.response}')

    # Assistantと会話するためのスラッシュコマンド
    @app_commands.command(name='ask_assistant', description='ffxについて教えてくれる')
    @app_commands.describe(message_text='送信するメッセージ')
    async def ask_assistant(self, ctx: discord.Interaction, message_text: str):
        # 実際の返答を即座に行えないため、仮の返答をする
        await ctx.response.defer()
        # OpenAI apiにアクセスし、結果を得る
        response = self.gpt.ask_ffx(ChatGPTRequest(message_text))
        await ctx.followup.send(f'ユーザー : {message_text}\n\nアシスタント : {response.response}')

