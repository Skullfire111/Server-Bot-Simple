import discord
import random
import v_of_torf
import helptxt
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')

@bot.command(pass_context=True)
async def h(ctx):
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
	for role.name in member.roles:
		if role.name != "<role>":
			await bot.say("Requesting promotion. Please wait for approval")
			await client.send_message(channel.<modonlychannelhere>, content=message.author "is requesting the <role name> role")
		else:
			await bot.say("You already are a <role>!")

@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_roles=True)
async def givememb(ctx, user = None, yorn = None):
	if yorn is None:
		await bot.say('Correct use of this function is: >setmemb <@person> <yes/no>')
	elif user is None:
		await bot.say('Correct use of this function is: >setmemb <@person> <yes/no>')
	else:
		if yorn is "yes":
			add_roles(user, '<role>')
			await client.send_message(user, content="Your request for <role name> has been granted!")
		elif yorn is "no":
			await client.send_message(user, content="Sorry, but your request for <role name> has been denied.")

@bot.command(pass_context=True)
async def r(ctx, redditi = None):
	if redditi is None:
		reddit = "```Use the >r branch of commands to bring up a post (or Subreddit) from Reddit:" + "\n"
		reddit += ">r all: Recent top posts from all of Reddit (clean)" + "\n"
		reddit += ">r random: A random post from all of Reddit (clean)" + "\n"
		reddit += ">r meme: A random post from the /r/memes Subreddit (possibly NSFW)" + "\n"
		reddit += "\n"
		reddit += "-Admins Only-" + "\n"
		reddit += ">memes: Toggle on/off random hourly posts from /r/memes" + "\n"
		reddit += "```"
		await bot.say(reddit)
	elif redditi is "meme":
		await client.send_message(message.channel, content="Wow, a random meme appeared from */r/memes*!", embed="www.reddit.com/r/memes/random")
	elif redditi is "random":
		await client.send_message(message.channel, content="Get your daily dose of internet with a random *clean* post from Reddit!", embed="www.reddit.com/random")
	elif redditi is "all":
		await client.send_message(message.channel, content="Find your thing with recent top *clean* posts from **all** of Reddit!", embed="www.reddit.com/random")
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_server=True)
async def memes(ctx):
	torf = v_of_torf.torfv(change)
	if torf is True:
		m = 3600
		while m	> 0:
			if m > 0:
				await asyncio.sleep(1)
				m = m - 1
			if m == 0:
				await client.send_message(channel.memes, content=None, embed="www.reddit.com/r/memes/random")
				m = 3600
			break
	if torf is False:
		break
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(mute_user=True)
async def mute(ctx, user, hrs):
	if user is None:
		bot.say('Correct usage is: >mute <@person> <hours>')
	elif hrs is None:
		bot.say('Correct usage is: >mute <@person> <hours>')
	else:	
		time = hrs * 3600
		while t	> 0:
			if t > 0:
				asyncio.sleep(1)
				t = t - 1
		while t > 0:
			mute.muteuser(user)
		muted = user + "\n"
		muted += "was temorarily silenced for" + "\n"
		muted += hrs
		muted += "hours."
		await client.send_message(channel.report, content=muted)


bot.run("<token>")
