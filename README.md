# nextcord-ext-activities
| [Docs (from MaskDuck/nextcord-ext-activities)](https://nextcord-ext-activities.readthedocs.io) | [GitHub repo](https://github.com/argo0n/pycord-ext-activities) |<br>
pycord.ext.activities is an extension that helps you to launch activities on Discord. <br>

# Quick example
```py
import discord
from discord.ext import activities, commands

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"Logged in as {str(bot.user)} (ID {bot.user.id})")


@bot.command()
async def poker(ctx, channel: discord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.poker)
    await ctx.send(invite_link.url)


@bot.command()
async def betrayal(ctx, channel: discord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.betrayal)
    await ctx.send(invite_link.url)


bot.run("token here")
```
You can find more example in the [example directory](https://github.com/argo0n/pycord-ext-activities/tree/main/examples).

[![Powered by Pycord](https://custom-icon-badges.herokuapp.com/badge/-Powered%20by%20Pycord-0d1620?logo=pycord)](https://github.com/Pycord-Development/pycord "Powered by Pycord Python API Wrapper")
