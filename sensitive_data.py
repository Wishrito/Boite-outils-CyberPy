import os


class SecurizedClass:
    """Base class for handling the discord bot token and some other environnment variables."""

    def __init__(self):
        self.DISCORD_TOKEN = str(os.getenv("discord_token"))
