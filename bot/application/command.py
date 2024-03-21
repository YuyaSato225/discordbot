import discord
from discord.ext import commands
from discord import app_commands
from ..Usecases.ChatGPTClient import ChatGPTClient
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='test', description='あいさつをするよ')
    async def test(self, ctx: discord.Interaction):
        await ctx.response.send_message('おはようございます！')

    @app_commands.command(name='chat', description='ChatGPTと会話できます')
    @app_commands.describe(message_text='送信するメッセージ')
    async def chat(self, ctx: discord.Interaction, message_text: str):
        await ctx.response.defer()
        gpt = ChatGPTClient()
        response = gpt.send_request(message_text)
        await ctx.followup.send(response)
