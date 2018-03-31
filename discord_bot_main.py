import discord
import praw
import random
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
	global ml
	global mr

	torf = False
	pmr = 307110698322886658
	memes = 420307378093817856
	report = 410902743515922432
	ml = 421900373507309569
	mr = 429730346251190283
	
	mlc = bot.get_channel(ml)
	lm = 'Logged in as **'
	lm += bot.user.name
	lm += ', '
	lm += str(bot.user.id)
	lm += '** using `'
	lm += discord.__version__
	lm += '`'
	await mlc.send(lm)

@bot.event
async def on_message_delete(message):
	mrc = bot.get_channel(mr)
	channel = message.channel.mention

	mc = 'Deleted Message in '
	mc += channel
	mc += ':'

	em = discord.Embed(title=mc, description=message.content, colour=0xe74c3c)
	em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
	try:
		if votearrow.content.startswith('https://'):
			em.set_image(url=message.content)
			breakstar = False
	except:
		pass
	try:
		attach = message.attachments
		em.set_image(url = attach[0].url)
		breakstar = False
	except:
		pass

	await mrc.send(embed = em)

@bot.event
async def on_message_edit(message, after):
	mrc = bot.get_channel(mr)
	if after.channel is mrc:
		pass
	else:
		channel = message.channel.mention

		mc = 'Edited Message in '
		mc += channel
		mc += ':'

		me = 'Old Message: \n \n'
		me += message.content
		me += '\n \n \n'
		me += 'New Message: \n \n'
		me += after.content

		em = discord.Embed(title=mc, description=me, colour=0xFFD700)
		em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		try:
			if message.content.startswith('https://'):
				em.set_image(url=message.content)
				breakstar = False
		except:
			pass
		try:
			attach = message.attachments
			em.set_image(url = attach[0].url)
			breakstar = False
		except:
			pass

		await mrc.send(embed = em)

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
	await ctx.send(helpm)

@bot.command()
async def clap(ctx, *, sentence : str = None):
    if sentence is None:
        await ctx.send('You have to say something before this command works')
    else:
        sentence = sentence.replace(' ', ':clap:')
        sentence += ':clap:'
        await ctx.send(sentence)

@bot.command()
async def smh(ctx, *, headshake : str = None):
	if headshake is None:
		await ctx.send('You have to say something before this command works')
	else:
		headshake = headshake.replace('smh', 'shaking my smh')
		headshake += ' smh'
		await ctx.send(headshake)

@bot.command(pass_context=True)
async def role(ctx):
	for role.name in member.roles:
		if role.name != "Member":
			await ctx.send("You already are a Member!")
		else:
			await ctx.send("Requesting promotion. Please wait for approval")
			mm = message.author
			mm+= 'is requesting to be a Member'
			await client.send_message(pmr, mm)

@bot.command(pass_context=True)
async def givememb(ctx, user = None, yorn = None):
	if yorn is None:
		await ctx.send('Correct use of this function is: >setmemb <@person> <yes/no>')
	elif user is None:
		await ctx.send('Correct use of this function is: >setmemb <@person> <yes/no>')
	else:
		if yorn is "yes":
			add_roles(user, 'Member')
			await user.send("Your request for Member has been granted!")
		elif yorn is "no":
			await user.send("Sorry, but your request for Member has been denied.")
		else:
			await ctx.send('You do not have permission to use this command!')

@bot.command()
async def r(ctx, ri : str = None):
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
			subreddit = reddit.subreddit('me_irl')
			submission = subreddit.get_random_submission
			meme = submission.url
			await ctx.send("Wow, a random meme appeared from */r/me_irl*!")
			await ctx.send(meme)
		elif ri is "random":
			subreddit = reddit.subreddit('all')
			submission = subreddit.get_random_submission
			random = submission.url
			await ctx.send("Get your daily dose of internet with a random *clean* post from Reddit!")
			await ctx.send(random)
		elif ri is "all":
			await ctx.send("Find your thing with recent top *clean* posts from **all** of Reddit!")
			subreddit = reddit.subreddit('all')
			for i in subreddit.hot(limit = 5):
				all = i.url
				await ctx.send(all)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def memes(ctx):
	memechannel = bot.get_channel(memes)
	if torf is True:
		ctx.send('The \"Hourly Memes\" function has been toggled on.')
		torf = False
		while True:
			subreddit = reddit.subreddit('me_irl')
			submission = subreddit.get_random_submission
			meme = submission.url
			await memechannel.send(meme)
			await asyncio.sleep(3600)
	else:
		await ctx.send('The \"Hourly Memes\" function has been toggled off.')
		torf = True
		
@memes.error
async def memes_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.send(':x: You do not have permission to use this command!')

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.Member, tint :str = None, tdenom :str = None, *, reason : str = None):
	if tdenom in ['s', 'm', 'h', 'd']:
		if user is ' ':
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		elif tint is ' ':
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		elif tdenom is ' ':
			await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
		else:
			role = discord.utils.get(ctx.guild.roles, name='Muted')
			if role in user.roles:
				umention = user.mention
				already = umention
				already += ' has already been muted'
				await ctx.send(already)
			else:
				await user.add_roles(role)
				umention = user.mention
				muted = umention
				muted += ' was muted for '
				muted += tint
				muted += tdenom
				muted += ' Reason: `'
				muted += reason
				muted += '`'
				mchannel = bot.get_channel(report)
				mlc = bot.get_channel(ml)
				await ctx.send(muted)
				await mchannel.send(muted)
				await mlc.send(muted)
				if tdenom is 's':
					time = 1
				elif tdenom is 'm':
					time = 60
				elif tdenom is 'h':
					time = 3600
				elif tdenom is 'd':
					time = 86400
				t = tint * time
				await asyncio.sleep(t)
				await user.remove_roles(role)
	else:
		await ctx.send('Correct usage is: >mute <@person> <time integer> <s/m/h/d> <reason(optional)>')
	
@mute.error
async def mute_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.send(':x: You do not have permission to use this command!')
	elif isinstance(error, discord.Forbidden):
		await ctx.send(':x: Error 403: You are forbidden from using that command!')
	else:
		print(error)

bot.run("<token>")
