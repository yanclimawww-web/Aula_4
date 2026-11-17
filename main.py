
import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

xp = 0
nivel = 1

pontos_ambientais = {}

# Comando para regar a árvore
@bot.command(name="regar")
async def regar(ctx):
    global xp, nivel

    xp += 10
    subiu_nivel = False

    if xp >= 50:
        xp -= 50
        nivel += 1
        subiu_nivel = True

    embed = discord.Embed(
        title="🌳 Árvore regada!",
        description="Você cuidou da sua árvore!",
        color=discord.Color.green()
    )

    embed.add_field(name="💧 XP ganho", value="+10 XP", inline=True)
    embed.add_field(name="⭐ Nível", value=str(nivel), inline=True)
    embed.add_field(name="🌱 XP atual", value=f"{xp}/50", inline=True)

    if subiu_nivel:
        embed.add_field(
            name="🎉 Parabéns!",
            value="Sua árvore subiu de nível!",
            inline=False
        )

    embed.set_footer(text="Continue cuidando do meio ambiente!")

    await ctx.send(embed=embed)


# Comando para reciclar materiais
@bot.command(name="reciclar")
async def reciclar(ctx, material: str):
    materiais = ["papel", "plastico", "vidro", "metal"]

    if material.lower() not in materiais:
        await ctx.send(
            "Material inválido! Use papel, plastico, vidro ou metal."
        )
        return

    pontos_ambientais[ctx.author.id] = (
        pontos_ambientais.get(ctx.author.id, 0) + 10
    )

    embed = discord.Embed(
        title="♻️ Reciclagem realizada!",
        description=f"Você reciclou **{material}**!",
        color=discord.Color.green()
    )

    embed.add_field(name="🌱 Pontos ganhos", value="+10 pontos", inline=True)

    embed.add_field(
        name="🏆 Total de pontos",
        value=str(pontos_ambientais[ctx.author.id]),
        inline=True
    )

    embed.set_footer(text="Cuide do meio ambiente!")

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")


bot.run("Seu_Token")
