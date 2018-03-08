import discord
import asyncio

def mute(tint, tdenom):
	if tdenom is 's':
		time = 1
	elif tdenom is 'm':
		time = 60
	elif tdenom is 'h':
		time = 3600
	elif tdenom is 'd':
		time = 86400
	t = tint * time
	while t > 0:
		t = t - 1
		asyncio.sleep(1)
		if t == 0:
			return t
