import asyncio
import sqlite3 as db
import tkinter as tk
from typing import Optional

import discord
from discord import app_commands

from sensitive_data import SecurizedClass


class DiscordClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = DiscordClient(intents=discord.Intents.all())

dbGroup = app_commands.Group(name="config", description="configuration de la base de données",
                             default_permissions=discord.Permissions(administrator=True))


async def table_autocomplete(interaction: discord.Interaction, current: str):
    connexion = db.connect("./database/db.sqlite")
    cursor = connexion.cursor()
    cursor.execute(f"SELECT * FROM {current}")
    result = cursor.fetchone()
    return [
        app_commands.Choice(name=table_name, value=table_name)
        for table_name in result
    ]


@dbGroup.command(name="custom_request", description="make a request to the database")
@app_commands.autocomplete(table=table_autocomplete)
@app_commands.describe(request_type="the request type", table="the table name", input_field="the values, if any")
@app_commands.choices(request_type=[
    app_commands.Choice(name="Insert", value="INSERT"),
    app_commands.Choice(name="Select", value="SELECT"),
    app_commands.Choice(name="Update", value="UPDATE"),
    app_commands.Choice(name="Delete", value="DELETE"),
    app_commands.Choice(name="Create", value="CREATE"),
    app_commands.Choice(name="Drop", value="DROP")
])
async def custom_request(interaction: discord.Interaction, request_type: app_commands.Choice[str], table: str, input_field: Optional[str]):
    connexion = db.connect("./database/db.sqlite")
    cursor = connexion.cursor()
    msg = ""
    request = ""
    match request_type.value:
        case "INSERT":
            if type(input_field) == str:
                request = f"INSERT INTO {table} VALUES ({input_field})"
                cursor.execute(request)
                connexion.commit()
                connexion.close()
            if type(input_field) == None:
                msg = "Veuillez renseigner une valeur"
        case "SELECT":
            result = cursor.execute(request)
            if result:
                for row in result:
                    await interaction.response.send_message(row)
            connexion.close()

        case "UPDATE":
            if type(input_field) == str:
                request = f"UPDATE {table} SET {input_field}"
                cursor.execute(request)
                connexion.commit()
                connexion.close()
            if type(input_field) == None:
                msg = "Veuillez renseigner une valeur"
        case "DELETE":
            if type(input_field) == str:
                request = f"DELETE FROM {table} WHERE {input_field}"
                cursor.execute(request)
                connexion.commit()
                connexion.close()
            if type(input_field) == None:
                msg = "Veuillez renseigner une valeur"
        case "CREATE":
            if type(input_field) == str:
                request = f"CREATE TABLE IF NOT EXISTS {table} ({input_field})"

            if type(input_field) == None:
                msg = "Veuillez renseigner une valeur"
        case "DROP":
            if type(input_field) == str:
                request = f"DROP TABLE IF EXISTS {table}"
                msg = ""

            if type(input_field) == None:
                msg = "Veuillez renseigner une valeur"

            cursor.execute(request)
            connexion.commit()
            connexion.close()


async def on_ready():
    print(f"Logged in as {client.user}")


if __name__ == "__main__":
    connexion = db.connect("./database/db.sqlite")
    cursor = connexion.cursor()
    requests = [
        "CREATE TABLE IF NOT EXISTS MailsConfig (MailsBody STRING NOT NULL DEFAULT \"Bonjour\", MailsSubject STRING NOT NULL \"Agrandir votre b*\")"
    ]

    for request in requests:
        cursor.execute(request)
    connexion.commit()
    connexion.close()
    client.run(SecurizedClass().DISCORD_TOKEN)
