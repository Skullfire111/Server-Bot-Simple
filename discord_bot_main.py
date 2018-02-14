import discord
import random
import v_of_torf
import helptxt
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')

@bot.command(pass_context=True)
async def help(ctx):
	helptxt.run(h)
		
@bot.command(pass_context=True)
async def clap(ctx, *, sentence : str = None):
    if sentence is None:
        await bot.say('You have to say anything before this command works')
    else:
        sentence = sentence.replace(' ', ':clap:')
        await bot.say(sentence)
					
@bot.command(pass_context=True)
async def <role>(ctx):
	if ctx is "<role>":
		user = message.author
		for member.roles:
			if role.name not "<role>":
				await bot.say("Requesting promotion. Please wait for approval")
				for role.name(<moderator>)
					await client.send_message(channel.privat_mod_room, content=user + "is requesting the <role name> role", *, tts=False, embed=None)
			else await bot.say("You are already a <role>!")

@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_roles=True)
async def givememb(ctx, user = None, yorn = None):
	if yorn is None or if user is None:
		await bot.say('Correct use of this function is: >setmemb <@person> <yes/no>'):
	else:
		if yorn is "yes":
			add_roles(user, <role>)
			await client.send_message(user, content="Your request for <role name> has been granted!", *, tts=False, embed=None)
		elif yorn is "no":
			await client.send_message(user, content="Sorry, but your request for <role name> has been denied.", *, tts=False, embed=None)

@bot.command(pass_context=True)
async def r(ctx):
	if ctx == "rmeme":
		await client.send_message(message.channel, content="Wow, a random meme appeared from */r/memes*!", *, tts=False, embed="www.reddit.com/r/memes/random")
        if ctx == "rrandom":
		await client.send_message(message.channel, content="Get your daily dose of internet with a random *clean* post from Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == "rall":
		await client.send_message(message.channel, content="Find your thing with recent top *clean* posts from **all** of Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == "r":
		reddit = "```Use the >r branch of commands to bring up a post (or Subreddit) from Reddit:" + "\n"
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
async def mute(ctx, user = None, hrs = None):
	if user is None or if hrs is None:
		bot.say('Correct usage is: >mute <@person> <hours>
	else:
		t = hrs * 3600
		while t	> 0:
			if t > 0:
				await asyncio.sleep(1)
				t = t - 1
			while t > 0:
				if message.author is user:
					await client.delete_message(message)
		await client.send_message(report, content=user "**was temporarily silenced for" x "hours**"`, *, tts=False, embed=None)

bot.run("<token>")

#make sure to run in a terminal using the latest python while connected to the internet, or the bot will not be online
