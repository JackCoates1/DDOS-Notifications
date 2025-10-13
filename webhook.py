# Network - Attack Logs
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import yaml
import sys
import os

def load_config():
    """Load configuration from config.yaml file."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    
    if not os.path.exists(config_path):
        print("ERROR: config.yaml not found!")
        print("Please copy config.yaml.example to config.yaml and fill in your details.")
        print(f"Expected location: {config_path}")
        sys.exit(1)
    
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except yaml.YAMLError as e:
        print(f"ERROR: Failed to parse config.yaml: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to read config.yaml: {e}")
        sys.exit(1)

# Load configuration
config = load_config()

# Create webhook with configuration
webhook = DiscordWebhook(
    url=config['webhook']['url'],
    username=config['webhook']['username']
)

# Create embed with configuration
embed = DiscordEmbed(
    title=config['embed']['title'],
    url=config['embed']['url'],
    description=config['embed']['description'],
    color=config['embed']['color']
)

# Set timestamp
embed.set_timestamp()

# Add embed fields
embed.add_embed_field(
    name='**Protection Provider:**',
    value=config['embed']['fields']['protection_provider']
)
embed.add_embed_field(
    name='**Location:**',
    value=config['embed']['fields']['location']
)
embed.add_embed_field(
    name='**IP Address:**',
    value=config['embed']['fields']['ip_address']
)

# Set thumbnail
embed.set_thumbnail(url=config['embed']['thumbnail_url'])

# Set footer
embed.set_footer(text=config['embed']['footer_text'])

# Send webhook
webhook.add_embed(embed)
response = webhook.execute()


