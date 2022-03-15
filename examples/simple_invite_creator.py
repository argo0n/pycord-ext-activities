import nextcord
from nextcord.ext import activities, commands

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"Logged in as {str(bot.user)} (ID {bot.user.id})")


@bot.command()
async def poker(ctx, channel: nextcord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.poker)
    await ctx.send(invite_link.url)


@bot.command()
async def betrayal(ctx, channel: nextcord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.betrayal)
    await ctx.send(invite_link.url)


bot.run("token here")
