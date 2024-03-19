import discord
from discord import app_commands 
from .. import config

# Botの接続と動作設定
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():  
    print('ログインしました') 
    await client.change_presence(activity=discord.Game(new_activity)) 
    # スラッシュコマンドを同期 
    await tree.sync()

@tree.command(name='test', description='Say hello to the world!') 
async def test(interaction: discord.Interaction): 
    await interaction.response.send_message('Hello, World!')

# Botのトークンを設定
client.run(config.DISCORD_BOT_TOKEN)

