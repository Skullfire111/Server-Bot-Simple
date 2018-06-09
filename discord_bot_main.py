import discord
import random
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')

bot.remove_command('help')

@bot.event
async def on_ready():
	print('Logged in...')
	print(discord.__version__)
	print('-----')

	global report
	global modlog
	global bestof
	global worstof
	global guild
	global owner

	report = 410902743515922432
	modlog = 421900373507309569
	bestof = 420038191329050634
	worstof = 421509130235412480
	guild = 302191095184621568
	owner = 283353337292783616
	
	modlogchannel = bot.get_channel(modlog)
	lm = 'Logged in as: \n **'
	lm += bot.user.display_name
	lm += '** \n **'
	lm += str(bot.user.id)
	lm += '** \n \n Using: \n `'
	lm += 'discord.py version '
	lm += discord.__version__
	lm += '`'
	
	em = discord.Embed(title=':white_check_mark: **CONECTED**', description=lm, colour=0x9b59b6)
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
	if member == message.guild.owner_id:
		if reaction.name == '⭐':
			if str(messageid) in open('bestof.txt').read():
				pass
			else:
				mt = ':ok_hand: Good Post :ok_hand:'

				mc = message.content

				em = discord.Embed(title=mt, description=mc, colour=0xbc52ec)
				em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
				em.set_footer(text='This meme recieved a star from {}!'.format(message.guild.owner.display_name))
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
					mt = ':ok_hand: Good Post :ok_hand:'

					mc = message.content

					em = discord.Embed(title=mt, description=mc, colour=0xbc52ec)
					em.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
					em.set_footer(text='This meme recieved enough stars to make it into #bestof')
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
	else:
		pass


@bot.event
async def on_message_delete(message):
	if message.author.bot is True:
		return
	modlogchannel = bot.get_channel(modlog)
	channel = message.channel.name

	mt = 'Deleted Message in #{}:'.format(channel)

	mc = message.content

	em = discord.Embed(title=mt, description=mc, colour=0xe74c3c)
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
		return
	elif message == after:
		return
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
async def help(ctx):
	b = bot.user.display_name
	helpt = "Commands for "
	helpt += b
	helpt += ": \n \n"

	helpm = """**FUN COMMANDS:**
	`>clap <message>`: sends a fun message with clap emojis
	`>mock <message>`: sends a fun message with letters randomly turned uppercase and lowercase
	
	**UTILITY COMMANDS:**
	`>roles [user]`: sends the list of roles for the server, or for the specified user, along with their IDs \n
	
	**MODERATION ONLY:**
	`>mute <user> <s/m/h/d> [reason]`: mutes the user for the specified amount of time
	`>unmute <user>`: unmutes the specified muted user
	
	*<> = necessary          [] = optional*"""

	em = discord.Embed(title=helpt, description=helpm, colour=0x9b59b6)
	em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

	await ctx.send(embed=em)

@bot.command()
async def clap(ctx, *, sentence : str = None):
	if sentence is None:
		await ctx.send('You have to say something before this command works')
	else:
		sentencetemp = sentence.replace(' ', ':clap:')
		sentence = ':clap:'
		sentence += sentencetemp
		sentence += ':clap:'
		await ctx.send(sentence)

@bot.command()
async def smh(ctx, *, headshake : str = None):
	if headshake is None:
		await ctx.send('You have to say something before this command works')
	else:
		headshake = headshake.replace('smh', 'smh my head')
		headshake += ' smh'
		await ctx.send(headshake)

@bot.command()
async def mock(ctx, *, mocktxt : str = None):
	if mocktxt == None:
		await ctx.send('You have to say something before this command works')
	else:
		list = []
		for i in mocktxt:
			list += i
			for i in range(len(list)):
				p = random.randint(1, 100)
				if p < 51:
					list[i] = list[i].lower()
				else:
					list[i] = list[i].upper()
		mocktxtnew = ''
		for i in list:
			mocktxtnew += i
		await ctx.send(mocktxtnew)

@bot.command()
async def moan(ctx):
	x = random.choice([1, 2, 3, 4])
	if x == 1:
		moan = '***OOOoOOOOOOooOoOhHh***'
	if x == 2:
		moan = '***AaaAAAAAaaaaAAAA***'
	if x == 3:
		moan = '***UUUUUuuuUuUUuUUUuUUUUhhhhhhh***'
	if x == 4:
		if random.random() < 0.1:
			moan = '***Uuuhh UUH UuH AAh OOh Uuh YuuuHHHH MMMMMMMMMH***'
		else:
			moan = random.choice(['***OOOoOOOOOOooOoOhHh***', '***AaaAAAAAaaaaAAAA***', '***UUUUUuuuUuUUuUUUuUUUUhhhhhhh***'])
	await ctx.send(moan)

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
