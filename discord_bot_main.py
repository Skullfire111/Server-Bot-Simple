import discord
import random
import mute
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')
@bot.event
async def on_ready():
	print('Logged in...')
	print(discord.__version__)
	print('-----')

	global memes
	global pmr
	global report
	global torf

	torf = False
	pmr = "307110698322886658"
	memes = "420307378093817856"
	report = "410902743515922432"

@bot.command(pass_context=True)
async def h(ctx):
	helpm = "```-------------------------Help Guide-------------------------" + "\n"
	helpm += "\n"
	helpm += "---------------Roles---------------" + "\n"
	helpm += ">member: Checks if you have the 'Wet Memer' role" + "\n"
	helpm += "         Also can be used to request the role" + "\n"
	helpm += "\n"
	helpm += ">setmemb: An Admin-only command used to grant membership" + "\n"
	helpm += "\n"
	helpm += "---------------Fun Commands---------------" + "\n"
	helpm += "\n"
	helpm += ">clap <message>: Turns the spaces in any message to clap emojis" + "\n"
	helpm += "\n"
	helpm += ">r: Shows the Reddit-command help menu" + "\n"
	helpm += "\n"
	helpm += ">rall: Recent top posts from all of Reddit (clean)" + "\n"
	helpm += "\n"
	helpm += ">rrandom: A random post from all of Reddit (clean)" + "\n"
	helpm += "\n"
	helpm += ">rmeme: A random post from the /r/memes Subreddit (possibly NSFW)" + "\n"
	helpm += "" + "\n"
	helpm += "---------------Admin and Mod Commands---------------" + "\n"
	helpm += "\n"
	helpm += ">memes: Toggle on/off random hourly posts from /r/memes" + "\n"
	helpm += "\n"
	helpm += ">mute: Used to temporarily mute any amount of hours" + "\n"
	helpm += "       The number of hours you wish to mute someone must be an integer" + "\n"
	helpm += "```"
	await bot.say(helpms)

@bot.command(pass_context=True)
async def clap(ctx, *, sentence : str = None):
    if sentence is None:
        await bot.say('You have to say something before this command works')
    else:
        sentence = sentence.replace(' ', ':clap:')
        sentence += ':clap:'
        await ctx.send(sentence)

@bot.command(pass_context=True)
async def role(ctx):
	for role.name in member.roles:
		if role.name != "Member":
			await bot.say("You already are a Member!")
		else:
			await bot.say("Requesting promotion. Please wait for approval")
			mm = message.author
			mm+= 'is requesting to be a Member'
			await client.send_message(pmr, mm)

@bot.command(pass_context=True)
async def givememb(ctx, user = None, yorn = None):
	if yorn is None:
		await bot.say('Correct use of this function is: >setmemb <@person> <yes/no>')
	elif user is None:
		await bot.say('Correct use of this function is: >setmemb <@person> <yes/no>')
	else:
		if yorn is "yes":
			add_roles(user, 'Member')
			await bot.send_message(user, "Your request for Member has been granted!")
		elif yorn is "no":
			await bot.send_message(user, "Sorry, but your request for Member has been denied.")
		else:
			await bot.say('You do not have permission to use this command!')
	
@bot.command()
async def r(ctx, ri = None):
	if ri is None:
		reddit = "```Use the >r branch of commands to bring up a post (or Subreddit) from Reddit:" + "\n"
		reddit += ">r all: Recent top posts from all of Reddit (clean)" + "\n"
		reddit += ">r random: A random post from all of Reddit (clean)" + "\n"
		reddit += ">r meme: A random post from the /r/memes Subreddit (possibly NSFW)" + "\n"
		reddit += "\n"
		reddit += "-Admins Only-" + "\n"
		reddit += ">memes: Toggle on/off random hourly posts from /r/memes" + "\n"
		reddit += "```"
		await ctx.send(reddit)
	else:
		if ri is "meme":
			meme = "Wow, a random meme appeared from */r/me_irl*!\n"
			em = "www.reddit.com/r/me_irl/random"
			await ctx.send(message.channel, meme, embed=em)
		elif ri is "random":
			random = "Get your daily dose of internet with a random *clean* post from Reddit!\n"
			em = "www.reddit.com/random"
			await ctx.send(message.channel, random, embed=em)
		elif ri is "all":
			all = "Find your thing with recent top *clean* posts from **all** of Reddit!\n"
			em = "www.reddit.com/all"
			await ctx.send(message.channel, all, embed=em)
	
@bot.command()
@commands.has_permissions(manage_messages=True)
async def memes(ctx):
	if torf is True:
		bot.say('The \"Hourly Memes\" function has been toggled on.')
		m = 3600
		while m	> 0:
			if m > 0:
				await asyncio.sleep(1)
				m = m - 1
				if m == 0:
					memechannel = bot.get_channel(memes)
					em = "www.reddit.com/r/me_irl/random"
					await bot.send_message(memechannel, embed=em)
					m = 3600
		torf = False
	else:
		await bot.say('The \"Hourly Memes\" function has been toggled off.')
		torf = True
		
@memes.error
async def memes_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.send(':x: You do not have permission to use this command!')
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user = None, tint = None, tdenom = None, reason = None):
	await ctx.send('The command went through.')
	if tdenom in ['s', 'm', 'h', 'd']:
		if user is None:
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		elif tint is None:
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		elif tdenom is None:
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		else:
			role = discord.utils.get(ctx.guild.roles, name='Muted')
			if role in user.roles:
				await ctx.send(user, 'has already been muted')
			else:
				await user.add_roles(role)
				muted = user
				muted+= "was muted for" 
				muted += tint
				muted += tdenom
				muted += reason
				mutedchannel = bot.get_channel(report)
				await ctx.send(mutedchannel, muted)
				tr = mute.mute(tint, tdenom)
				if tr is 0:
					await user.remove_roles(role)
	else:
		bot.say('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
	
@mute.error
async def mute_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.send(':x: You do not have permission to use this command!')


bot.run("<token>")
