import discord
from discord.ext import commands
from functions import morse, log
from config import client_token, cmd_prefix

client = commands.Bot(command_prefix=cmd_prefix)


@client.event
async def on_ready():
    print("Ready")


@client.command()
async def mor(msg, *, arg):
    morse_embed = discord.Embed()
    morse_embed.add_field(name="Text", value=arg, inline=False)
    morse_embed.add_field(name="Morse", value=morse(arg), inline=True)
    await msg.send(embed=morse_embed)


@client.event
async def on_message(msg):
    if msg.author == client.user:
        await client.process_commands(msg)
    log(f'{str(msg.guild.name)}  -  {str(msg.author)}  =  {str(msg.content)}\n')
    await client.process_commands(msg)


client.run(client_token)
