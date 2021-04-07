from discord.ext import commands
import typing
import DiscordUtils

bot = commands.Bot(command_prefix='!')

@bot.command()
async def code(ctx):
    await ctx.send('testowa wiadomość')

@bot.command(pass_context=True)
@commands.has_role("Admin") # This must be exactly the name of the appropriate role
async def addrole(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Test")
    await bot.add_roles(member, role)

bot.run('ODI4OTQxMTM4NTgwODY1MDM0.YGw5mA.umuG2LnYjeLhKX4GAIpk7Tda8QQ')
