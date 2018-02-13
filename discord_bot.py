import discord
import random
import v_of_torf
import helptxt
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')

@bot.command(pass_context=True)
async def help(h):
	if h == "" or if h == "h" or if h == "help":
		helptxt.run(h)
	

@bot.command(pass_context=True)
async def role(ctx):
	if ctx == "<role>":
		user = message.author
		for member.roles:
			if role.name != "<role name>":
				await bot.say("Requesting promotion. Please wait for approval")
				for role.name(<moderator>)
					await client.send_message(channel.privat_mod_room, content=user + "is requesting the <role name> role", *, tts=False, embed=None)
			else await bot.say("You are already a <role>!")

@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_roles=True)
async def roleapprv(ctx, user, yorn):
	if ctx == "setmemb":
		if yorn == "yes":
			add_roles(user, <role>)
			await client.send_message(user, content="Your request for <role name> has been granted!", *, tts=False, embed=None)
		elif yorn == "no":
			await client.send_message(user, content="Sorry, but your request for <role name> has been denied.", *, tts=False, embed=None)
	
@bot.command(pass_context=True)
async def redd(ctx):
	if ctx == "rmeme":
		await client.send_message(message.channel, content="Wow, a random meme appeared from */r/memes*!", *, tts=False, embed="www.reddit.com/r/memes/random")
        if ctx == "rrandom":
		await client.send_message(message.channel, content="Get your daily dose of internet with a random *clean* post from Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == "rall":
		await client.send_message(message.channel, content="Find your thing with recent top *clean* posts from **all** of Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == "r":
		reddit = "```Use the >r command to bring up a post (or Subreddit) from Reddit:" + "\n"
		reddit += ">rall: Recent top posts from all of Reddit (clean)" + "\n"
		reddit += ">rrandom: A random post from all of Reddit (clean)" + "\n"
		reddit += ">rmeme: A random post from the /r/memes Subreddit (possibly NSFW)" + "\n"
		reddit += "\n"
		reddit += "-Admins Only-" + "\n"
		reddit += ">memes: Toggle on/off random hourly posts from /r/memes" + "\n"
		reddit += "```"
		await bot.say(reddit)
         
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_server=True)
async def memes(ctx):
	if ctx == "memes":
		torf = v_of_torf.torfv(change)
		if torf == True:
			m = 3600
			while m	> 0:
				if m > 0:
					await asyncio.sleep(1)
					m = m - 1
				if m == 0:
					await client.send_message(channel.memes, content=None, *, tts=False, embed="www.reddit.com/r/memes/random")
					m = 3600
				break
		if torf == False:
			break
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(mute_user=True)
async def mute(ctx, user, hrs):
	if ctx == "mute"
	t = hrs * 3600
	while t	> 0:
		if t > 0:
			await asyncio.sleep(1)
			t = t - 1
	while t > 0:
		if message.author == user:
			await client.delete_message(message)
	await client.send_message(report, content=user "**was temporarily silenced for" x "hours**"`, *, tts=False, embed=None)

bot.run("<token>")

#make sure to run in a terminal using the latest python while connected to the internet, or the bot will not be online
