import os


class SecurizedClass:
    """Base class for handling the discord bot token and some other environnment variables."""

    def __init__(self):
        pass

    @property
    def DISCORD_TOKEN(self) -> str:
        """Get the discord bot token from the environment variables.

        Returns:
        
            str: The discord bot token.
        """
        DISCORD_TOKEN = os.getenv("discord_token")

        try:
            return DISCORD_TOKEN if DISCORD_TOKEN is not None else ""
        except Exception as err:
            raise err
