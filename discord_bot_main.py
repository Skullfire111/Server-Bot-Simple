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
	global modlog
	global bestof
	global worstof
	global guild
	global modlist

	torf = False
	pmr = 307110698322886658
	memes = 420307378093817856
	report = 410902743515922432
	modlog = 421900373507309569
	bestof = 420038191329050634
	worstof = 421509130235412480
	guild = 302191095184621568
	modlist = []
	
	modlogchannel = bot.get_channel(modlog)
	lm = 'Logged in as: \n **'
	lm += bot.user.display_name
	lm += '** \n **'
	lm += str(bot.user.id)
	lm += '** \n \n using: \n `'
	lm += 'discord.py version '
	lm += discord.__version__
	lm += '`'
	
	em = discord.Embed(title=':white_check_mark: **CONECTED**', description=lm, colour=0x9900e5)
	em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

	await modlogchannel.send(embed=em)

@bot.event
async def on_member_join(member):
	if member.bot == True:
		return

	mc = 0
	for x in member.guild.members:
		if x.bot == False:
			mc += 1

	emt = 'Member Joined: \n \n'

	umention = member.mention
	des = '**Member:** '
	des += umention
	des += '\n'
	des += '**ID:** '
	des += str(member.id)
	des += '\n'
	des += '**Member Count:** '
	des += str(mc)
	des += '\n'

	em = discord.Embed(title=emt, description=des, colour=0x51cc72)
	em.set_author(name=member.display_name, icon_url=member.avatar_url)

	modlogchannel = bot.get_channel(modlog)
	await modlogchannel.send(embed = em)

@bot.event
async def on_member_remove(member):
	if member.bot == True:
		return

	mc = 0
	for x in member.guild.members:
		if x.bot == False:
			mc += 1

	emt = 'Member Left: \n \n'

	umention = member.mention
	des = '**Member:** '
	des += umention
	des += '\n'
	des += '**ID:** '
	des += str(member.id)
	des += '\n'
	des += '**Member Count:** '
	des += str(mc)
	des += '\n' 
	
	em = discord.Embed(title=emt, description=des, colour=0xe74c3c)
	em.set_author(name=member.display_name, icon_url=member.avatar_url)

	modlogchannel = bot.get_channel(modlog)
	await modlogchannel.send(embed = em)

@bot.event
async def on_raw_reaction_add(reaction, messageid, channelid, member):
	reactchannel = bot.get_channel(channelid)
	message = await reactchannel.get_message(messageid)
	if member == bot.user.id:
		return
	if message.author.bot == True:
		return
	bestofc = bot.get_channel(bestof)
	worstofc = bot.get_channel(worstof)
	if member == 283353337292783616:
		if reaction.name == '⭐':
			if str(messageid) in open('bestof.txt').read():
				pass
			else:
				mt = ':ok_hand: Good Meme :ok_hand:'

				mc = message.content

				em = discord.Embed(title=mt, description=mc, colour=0xbc52ec)
				em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
				try:
					if message.content.startswith('https://'):
						em.set_image(url=message.content)
				except:
					pass
				try:
					attach = message.attachments
					em.set_image(url = attach[0].url)
				except:
					pass	

				await bestofc.send(embed = em)
				cache = open("bestof.txt", "a+",encoding="utf8")
				cache.write(str(messageid) + " ")
				cache.close()

		if reaction.name == 'shitpost':
			if str(messageid) in open('worstof.txt').read():
				pass
			else:
				mt = '👺 Shitpost 👺'

				mc = message.content

				em = discord.Embed(title=mt, description=mc, colour=0x3f90ff)
				em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
				try:
					if message.content.startswith('https://'):
						em.set_image(url=message.content)
				except:
					pass
				try:
					attach = message.attachments
					em.set_image(url = attach[0].url)
				except:
					pass

				await worstofc.send(embed = em)
				cache = open("worstof.txt", "a+",encoding="utf8")
				cache.write(str(messageid) + " ")
				cache.close()
		elif reaction.count is 5:
			if reaction.name == '⭐':
				if str(messageid) in open('bestof.txt').read():
					pass
				else:
					print('bestof')
					mc = ':ok_hand: Good Meme :ok_hand:'

					em = discord.Embed(title=mc, description=message.content, colour=0xbc52ec)
					em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
					try:
						if message.content.startswith('https://'):
							em.set_image(url=message.content)
					except:
						pass
					try:
						attach = message.attachments
						em.set_image(url = attach[0].url)
					except:
						pass	

					await bestofc.send(embed = em)
					cache = open("bestof.txt", "a+",encoding="utf8")
					cache.write(str(messageid) + " ")
					cache.close()

			if reaction.name == 'shitpost':
				if str(messageid) in open('worstof.txt').read():
					pass
				else:
					mc = '👺 Shitpost 👺'

					em = discord.Embed(title=mc, description=message.content, colour=0x3f90ff)
					em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
					try:
						if message.content.startswith('https://'):
							em.set_image(url=message.content)
					except:
						pass
					try:
						attach = message.attachments
						em.set_image(url = attach[0].url)
					except:
						pass

					await worstofc.send(embed = em)
					cache = open("worstof.txt", "a+",encoding="utf8")
					cache.write(str(messageid) + " ")
					cache.close()
	else:
		pass


@bot.event
async def on_message_delete(message):
	if message.author.bot is True:
		return
	modlogchannel = bot.get_channel(modlog)
	channel = message.channel.name

	mc = 'Deleted Message in #'
	mc += channel
	mc += ':'

	em = discord.Embed(title=mc, description=message.content, colour=0xe74c3c)
	em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
	try:
		if message.content.startswith('https://'):
			em.set_image(url=message.content)
	except:
		pass
	try:
		attach = message.attachments
		em.set_image(url = attach[0].url)
	except:
		pass

	await modlogchannel.send(embed = em)

@bot.event
async def on_message_edit(message, after):
	modlogchannel = bot.get_channel(modlog)
	if message.author.bot is True:
		pass
	else:
		channel = message.channel.name

		mc = 'Edited Message in #'
		mc += channel
		mc += ':'

		me = '**Old Message:** \n'
		me += message.content
		me += '\n \n'
		me += '**New Message:** \n'
		me += after.content

		em = discord.Embed(title=mc, description=me, colour=0xFFD700)
		em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
		try:
			if message.content.startswith('https://'):
				em.set_image(url=message.content)
		except:
			pass
		try:
			attach = message.attachments
			em.set_image(url = attach[0].url)
		except:
			pass

		await modlogchannel.send(embed = em)

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

@bot.command()
async def roles(ctx, user : discord.Member = None):
	if user == None:
		rolelist = ''
		counter = 0
		for role in ctx.guild.roles:
			rolelist += str(role.id)
			rolelist += '   ---   '
			rolelist += role.name
			rolelist += '\n'
			counter += 1
	
		title = 'Roles in **'
		title += ctx.guild.name
		title += '**:'

		rolelist += '\n **'
		rolelist += str(counter)
		rolelist += ' roles**'

		em = discord.Embed(title=title, description=rolelist, colour=0x4cff30)
		await ctx.send(embed=em)

	else:
		umention = user.mention
		
		title = 'Roles for **'
		title += user.display_name
		title += '**:'
		
		rolelist = ''
		counter = 0
		for role in user.roles:
			rolelist += str(role.id)
			rolelist += '   ---   '
			rolelist += role.name
			rolelist += '\n'
			counter += 1
			
		rolelist += '\n **'
		rolelist += str(counter)
		rolelist += ' roles**'
		
		em = discord.Embed(title=title, description=rolelist, colour=0x4cff30)
		em.set_author(name=user.display_name, icon_url=user.avatar_url)	
		await ctx.send(embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.Member, tint :int = None, tdenom :str = None, *, reason : str = None):
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
				if reason is None:
					muted = umention
					muted += ' was muted for '
					muted += str(tint)
					muted += tdenom
				else:
					muted = umention
					muted += ' was muted for '
					muted += str(tint)
					muted += tdenom
					muted += ' (`'
					muted += reason
					muted += '`)'
				modlogchannel = bot.get_channel(modlog)
				mchannel = bot.get_channel(report)
				await modlogchannel.send(muted)
				await ctx.send(muted)
				await mchannel.send(muted)
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
				if role in user.roles:
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
		await ctx.send(error)
		print(error)
		
@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name='Muted')
	umention = user.mention
	if role in user.roles:
		await user.remove_roles(role)
		m = umention
		m += ' is no longer muted'
		await ctx.send(m)
	else:
		m = umention
		m += ' is not muted'
		await ctx.send(m)

@unmute.error
async def unmute_error(ctx, error):
	if isinstance(error, commands.errors.MissingPermissions):
		await ctx.send(':x: You do not have permission to use this command!')
	elif isinstance(error, discord.Forbidden):
		await ctx.send(':x: Error 403: You are forbidden from using that command!')
	else:
		await ctx.send(error)
		print(error)

bot.run("<token>")
