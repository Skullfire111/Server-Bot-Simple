import discord
import asyncio
from discord.ext import commands

async def run(h):
	help = "```---Help Guide---" + "\n"
	help += "\n"
	help += "-Roles-" + "\n"
	help += ">member: Checks if you have the 'Wet Memer' role" + "\n"
	help += "         Also can be used to request the role" + "\n"
	help += "\n"
	help += ">setmemb <@person> <yes/no>: An Admin-only command used to grant membership" + "\n"
	help += "\n"
	help += "-Fun Commands-" + "\n"
	help += "\n"
	help += ">clap <message>: Turns the spaces in any message to clap emojis" + "\n"
	help += "\n"
	help += ">r: Shows the Reddit-command help menu" + "\n"
	help += "\n"
	help += ">rall: Recent top posts from all of Reddit (clean)" + "\n"
	help += "\n"
	help += ">rrandom: A random post from all of Reddit (clean)" + "\n"
	help += "\n"
	help += ">rmeme: A random post from the /r/memes Subreddit (possibly NSFW)" + "\n"
	help += "" + "\n"
	help += "-Admin and Mod Commands-" + "\n"
	help += "\n"
	help += ">memes: Toggle on/off random hourly posts from /r/memes" + "\n"
	help += "\n"
	help += ">mute <@person> <hours>: Used to temporarily mute any amount of hours" + "\n"
	help += "       The number of hours you wish to mute someone must be an integer" + "\n"
	help += "```"
	await bot.say(help)
