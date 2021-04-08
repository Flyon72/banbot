from discord.ext import commands
import typing
import DiscordUtils

bot = commands.Bot(command_prefix='!')

@bot.command()
async def code(ctx):
    await ctx.send('testowa wiadomość')




