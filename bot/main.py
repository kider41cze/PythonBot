import discord
from discord.ext import commands
from functions import text2morse, log
from config import client_token, cmd_prefix

client = commands.Bot(command_prefix=cmd_prefix)


@client.event
async def on_ready():
    print("Ready")


@client.command(aliases=["nick", "nn"])
async def nickname(ctx, member: discord.Member, nick):
    if nick == "none":
        await member.edit(nick=None)
    else:
        await member.edit(nick=nick)


@client.command(aliases=["mor", "ms"])
async def morse(ctx, *, arg):
    morse_embed = discord.Embed()
    morse_embed.add_field(name="Text", value=arg, inline=False)
    morse_embed.add_field(name="Morse", value=text2morse(arg.upper()), inline=True)
    await ctx.send(embed=morse_embed)

    
@client.command(aliases=["remove", "c", "del"])
async def clear(ctx, limit : int):
    await ctx.channel.purge(limit=limit)
    await ctx.send(f"Deleted by {ctx.author.mention}")

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        await client.process_commands(ctx)
    log(f'{str(ctx.guild.name)}  -  {str(ctx.author)}  =  {str(ctx.content)}\n')
    print(f'{str(ctx.guild.name)}  -  {str(ctx.author)}  =  {str(ctx.content)}\n')
    await client.process_commands(ctx)


client.run(client_token)
