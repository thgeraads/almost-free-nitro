import discord
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f"Running on {client.user.name}#{client.user.discriminator}")
    await client.change_presence(afk=True, status=discord.Status.idle) 
@client.event
async def on_message(msg):
    if msg.author.id == client.user.id:
        message = msg.content
        match = re.search("\:(.*?)\:", message)
        if match:
            match_name = match.group(1)
            for guild in client.guilds:
                for emote in guild.emojis:
                    if emote.name == match_name:
                        if not isinstance(msg.channel, discord.channel.DMChannel):
                            if emote.guild_id == msg.guild.id:
                                return 
                            else:
                                await msg.edit(content=msg.content.replace(f":{match_name}:", f"{emote.url}?size=64"))
                        else:
                                await msg.edit(content=msg.content.replace(f":{match_name}:", f"{emote.url}?size=64"))
                                
client.run("<token>", bot=False)
