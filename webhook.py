# Insecurity Network - Attack Logs
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
NOW = datetime.now()
# Please place your webhook here.
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/812346710760226848/aTSDemQr8-iB7ijZ9Oi0Ceigbom-cdmlYYCMnGbUwnXzbl5wOGOCfTjBNA2F364_CM2x', username="Insecurity Network")
embed = DiscordEmbed(title='DDoS Alert (PPS Threshold Reached)', url='https://cybersniff.net', description='Insecuritys France OVH is underattack.', color=3447003)
embed.set_footer(text='Attack dump stored in: /home/ubuntu/dumps/')
embed.set_timestamp()
embed.add_embed_field(name='**Protection Provider:**', value='Shextys Firewall')
embed.add_embed_field(name='**Location:**', value='	Paris, France')
embed.add_embed_field(name='**IP Address:**', value='151.80.217.215')
embed.set_thumbnail(url='https://flaglane.com/download/french-flag/french-flag-medium.jpg')
embed.set_footer(text='Automatic Packet Dump has been initiated!')
webhook.add_embed(embed)
response = webhook.execute()
