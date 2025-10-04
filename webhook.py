# Insecurity Network - Attack Logs
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
NOW = datetime.now()
# Please place your webhook here.
webhook = DiscordWebhook(url='DISCORD WEBHOOK', username="USERNAME OF BOT")
embed = DiscordEmbed(title='DDoS Alert (PPS Threshold Reached)', url='https://cybersniff.net', description='DESCRIPTION OF MESSAGE', color=3447003)
embed.set_footer(text='Attack dump stored in: /home/ubuntu/dumps/')
embed.set_timestamp()
embed.add_embed_field(name='**Protection Provider:**', value='NAME OF PROIVDER')
embed.add_embed_field(name='**Location:**', value='LOCATION OF VPN')
embed.add_embed_field(name='**IP Address:**', value='151.80.217.215')
embed.set_thumbnail(url='https://flaglane.com/download/french-flag/french-flag-medium.jpg')
embed.set_footer(text='Automatic Packet Dump has been initiated!')
webhook.add_embed(embed)
response = webhook.execute()

