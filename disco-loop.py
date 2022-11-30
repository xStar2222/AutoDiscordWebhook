import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import time

with open("settings.json") as f:
    settings = json.load(f)

#Customize Webhook
def main():
    webhook = DiscordWebhook(url=settings['discordWebhook'])
    embed = DiscordEmbed()
    embed.set_title(f"TITLE")
    embed.set_description(f"DESCRIPTION")
    embed.set_timestamp()
    embed.set_color(0xFFFFFF)

    webhook.add_embed(embed)
    responce = webhook.execute()
    return

#Repeat The Webhook
while True:
    print("Starting Loop")
    main()
    time.sleep(10)
    
