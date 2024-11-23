import feedparser, time, settings
from discord import discord

webhook, whitelist, username, avatar_url, feed_url = discord.init_settings("nline")

feed = feedparser.parse(feed_url)
discord = discord(webhook, username, avatar_url, feed)

while 1:
    discord.prepare_and_notify()
    time.sleep(10)
