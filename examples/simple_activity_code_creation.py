import nextcord
from nextcord.ext import commands
from nextcord.ext import activities

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"Logged in as {str(bot.user)} (ID {bot.user.id})")


@bot.command()
async def poker(ctx, channel: nextcord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.poker)  # noqa: E501
    await ctx.send(invite_link)


@bot.command()
async def betrayal(ctx, channel: nextcord.VoiceChannel):
    invite_link = await channel.create_activity_invite(activities.Activity.betrayal)  # noqa: E501
    await ctx.send(invite_link)


bot.run('token here')
