import asyncio
from colorama import Fore, Style
import random
from discord.ext import commands
import discord
import sys

print(Fore.GREEN + "\nDisclaimer:\n")
print(Fore.YELLOW + "This is for educational purposes only.")
print(Fore.YELLOW + "Use this only if you have the consent of the server owner.")
print(Fore.YELLOW + "I am not responsible for any damage done by this bot.\n")

r = input(Fore.CYAN+"Continue?? (Y/N): ").lower()
if r == "y":
    print("Initializing Bot...")
elif r == "n":
    print(Style.RESET_ALL)
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    sys.exit(0)

token = "toke-here"  # INSERT U TOKEN

MSG = ["Thanks for use Clyde"]
MSG_CHANNEL = [
    "The server has been perfectly nuked! | **Support:**  https://dsc.gg/k-o-i `<3`"]

client = commands.Bot(command_prefix="-")  #PREFIX
client.remove_command("help")

@client.event
async def on_ready():
   print('''

██████╗░░█████╗░████████╗          ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝  ░░░░░░  ████╗░██║██║░░░██║██║░██╔╝██╔════╝
██████╦╝██║░░██║░░░██║░░░  █████╗  ██╔██╗██║██║░░░██║█████═╝░█████╗░░
██╔══██╗██║░░██║░░░██║░░░  ╚════╝  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██████╦╝╚█████╔╝░░░██║░░░  ░░░░░░  ██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═════╝░░╚════╝░░░░╚═╝░░░          ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝

  [+] Support Server: https://dsc.gg/k-o-i

''')
   while True:  # BUCLE
       await client.change_presence(activity=discord.Game(name="-help | -info"))
       await asyncio.sleep(15)
       await client.change_presence(activity=discord.Game(name="🍕 Eating pizza..."))
       await asyncio.sleep(15)
       await client.change_presence(activity=discord.Game(name="🍹 Drinking smoothies..."))
       await asyncio.sleep(15)
       await client.change_presence(activity=discord.Game(name="👋 and nuked your Discord-Server..."))
       await asyncio.sleep(15)
       

@client.command()
async def help(ctx):
    embed = discord.Embed(title = "Clyde", description = "My default prefix is `-`", )
    embed.add_field(name="My commands:", value="~ `-help` - See this message\n\n~ `-info` - See more info")
    embed.add_field(name="My commands [Admin]",
                    value="~ `channel` - Remove all channels\n\n~ `-roles` - Remove all roles\n\n ~ `-emojis` - Remove all emojis of server", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/914933674770853918/7ee5f4b74d52ed3bb5f89b74208019db.png?size=4096")   
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
            embed = discord.Embed(
                title="Information", description="I am a bot that serves to nuke servers")
            embed.add_field(
                name=f"Origin:", value="My creators created me with the utility of removing all channels, roles and emojis from your own server", inline=False)
            embed.add_field(
                name=f"Requirements:", value="For everything I mention, you will need to have the administrator role or be the creator of the server to use the bot", inline=False)
            embed.add_field(
                name=f"Data:", value="This bot is not made with bad intentions, what I am looking for is to automate some actions without the need to give more than 2 clicks\n ~ Type `-help` for more info", inline=False)

            await ctx.send(embed=embed)

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(
                title="Informacion", description="Soy un bot que sirve para nukear servers")
            embed.add_field(
                name=f"Funcionalidad:", value="Mis creadores me crearon con la utilidad de remover todos los canales, roles y emojis de tu propio servidor", inline=False)
            embed.add_field(
                name=f"Requisitos:", value="Para todo lo que mencione, necesitaras crear tu propio bot, solo el creador del bot podra dar uso al bot", inline=False)
            embed.add_field(
                name=f"Data:", value="Este bot no esta hecho con malas intenciones, lo que busco es automatisar algunas acciones sin necesidad de dar mas de 2 clicks", inline=False)

            await channel.send(embed=embed)
        break

@client.command()
@commands.is_owner()  # CAN ONLY BE USED BY THE BOT CREATOR
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN +
          f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
@commands.has_permissions(administrator= True)
async def channel(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
        
    await guild.create_text_channel("🔧┇ʟɪɢʜᴛ ɴᴜᴋᴇ"), print("The channel has been create")

@client.command()
# CAN ONLY BE USED BY THE BOT CREATOR
@commands.has_permissions(administrator=True)
async def emojis(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    return

@client.command()
@commands.has_permissions(administrator= True)  # CAN ONLY BE USED BY THE BOT CREATOR
async def roles(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    return


@client.event
async def on_guild_channel_create(ctx):
     await ctx.send(random.choice(MSG_CHANNEL))



client.run(token, bot=True)