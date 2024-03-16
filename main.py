import asyncio
import sqlite3 as db
import tkinter as tk
from typing import Optional

import discord
from discord import app_commands

from sensitive_data import SecurizedClass

guild_id = 1091096575280947404
guild_id1 = discord.Object(id=guild_id)
class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        await self.tree.sync(guild=guild_id1)


client = DiscordClient(intents=discord.Intents.all())

dbGroup = app_commands.Group(name="request", description="configuration de la base de données",
                             default_permissions=discord.Permissions(administrator=True))


async def table_autocomplete(interaction: discord.Interaction, current: str):
    connexion = db.connect("./database/db.sqlite")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    result = cursor.fetchone()
    return [
        app_commands.Choice(name=table_name, value=table_name)
        for table_name in result
    ]


@dbGroup.command(name="select", description="make a select request to the database")
@app_commands.describe(request_type="the request type", table="the table name", input_field="the values, if any")
@app_commands.autocomplete(table=table_autocomplete)
async def select_request(interaction: discord.Interaction, query: str, table: str, input_field: str, condition: Optional[str]):
    conneion = db.connect("./database/db.sqlite")
    cursor = conneion.cursor()
    request = f"SELECT {query} FROM {table}"
    if input_field and condition:
        request += f" WHERE {input_field} = {condition}"
    cursor.execute(request)
    response = cursor.fetchone()
    await interaction.response.send_message(response, ephemeral=True)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


if __name__ == "__main__":
    connexion = db.connect("./database/db.sqlite")
    cursor = connexion.cursor()
    requests = [
        "CREATE TABLE IF NOT EXISTS config (queries STRING)"
    ]

    for request in requests:
        cursor.execute(request)
    connexion.commit()
    connexion.close()
    client.run(SecurizedClass().DISCORD_TOKEN)
