import os
import discord
import dotenv
import API
import DALLe
import threading
import asyncio
import VEGA

dotenv.load_dotenv()

vega = VEGA.VEGA()

testBot = vega.testBot

if testBot:
    TOKEN = os.getenv('SNEK')
else:
    TOKEN = os.getenv('TOKEN')


intents = discord.Intents.all()

intents.messages = True
intents.members = True
intents.guilds = True



client = discord.Client(intents=intents)
GUILD = os.getenv('GUILD')

imageBot = DALLe.DALLe_Image_Bot()

# commands = ["$D", "$V", "$ TEST", "$ Status"]

def format_command(signal, user_command):
    split_str = user_command.split(signal, 1)

    if len(split_str) > 1:
        command_args = split_str[1]
        return command_args

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # DALL-E
    if message.content.startswith('$D '):
        input_str = message.content
        dalle_command = format_command('$D', message.content)

        imageBot.dalleCall(dalle_command)
        print(f"DALL-E Prompt: {dalle_command}")

        await message.channel.send(dalle_command)
        await message.channel.send(imageBot.image_url)

    # ChatGPT through VEGA
    if message.content.startswith('$V '):
        input_str = message.content
        vega_commnand = format_command('$V', message.content)
        API.gptCall(vega_commnand)
        await message.channel.send(API.content_output)


client.run(TOKEN)
