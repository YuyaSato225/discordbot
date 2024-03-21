import discord
from discord.ext import commands
from discord import app_commands
from ..Usecases.ChatGPTUsecase import ChatGPTUsecase
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse
from injector import inject


class CommandCog(commands.Cog):
    @inject
    def __init__(self, bot, gpt: ChatGPTUsecase):
        self.bot = bot
        self.gpt = gpt

    @app_commands.command(name='test', description='あいさつをするよ')
    async def test(self, ctx: discord.Interaction):
        await ctx.response.send_message('おはようございます！')

    @app_commands.command(name='chat', description='ChatGPTと会話できます')
    @app_commands.describe(message_text='送信するメッセージ')
    async def chat(self, ctx: discord.Interaction, message_text: str):
        await ctx.response.defer()
        response = self.gpt.send_request(ChatGPTRequest(message_text))
        await ctx.followup.send(response.response)
