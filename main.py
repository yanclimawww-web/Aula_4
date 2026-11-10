import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

xp = 0
nivel = 1

@bot.command(name="regar")
async def regar(ctx):
    global xp, nivel

    xp += 10

    if xp >= 50:
        xp -= 50
        nivel += 1

    await ctx.send(
        f"🌳 Você regou a árvore! XP: {xp}/50 | Nível: {nivel}"
    )

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

bot.run("token")
