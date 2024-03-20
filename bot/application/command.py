import discord
from discord.ext import commands
from discord import app_commands
from ..Usecases.ChatGPTClient import ChatGPTClient

class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='test', description='挨拶を返します。')
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message('こんにちは！')

    @app_commands.command(name='chat', description='ChatGPTと会話できます')
    @app_commands.describe(message_text='送信するメッセージ')
    async def chat(self, interaction: discord.Interaction, message_text: str):
        await interaction.response.defer()
        gpt = ChatGPTClient()
        response = gpt.send_request(message_text)
        await interaction.followup.send(response)
