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

# async def handle_command(command):
#     if command.startswith('test'):
#         # Handle test command
#         print("Test command")
#
#     elif command.startswith('exit'):
#         # Handle exit command
#         print("Exiting...")
#         await client.close()
#
#     else:
#         print("Unknown command")

def handle_input():
    while True:
        command = input("Enter command: ")
        asyncio.run(handle_command(command))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ Hello'):
        await message.channel.send("Hello, I am VEGA")

    if message.content.startswith('$TEST'):
        testPrompt = "Snoop Dogg riding a horse"
        imageBot.dalleCall(testPrompt)

        await message.channel.send(testPrompt)
        await message.channel.send(imageBot.image_url)


    if message.content.startswith('$$'):
        testPost = format_command('$$', message.content)
        print(testPost)

    if message.content.startswith('$D '):
        input_str = message.content
        dalle_command = format_command('$D', message.content)

        imageBot.dalleCall(dalle_command)
        print(f"DALL-E Prompt: {dalle_command}")

        await message.channel.send(dalle_command)
        await message.channel.send(imageBot.image_url)

    if message.content.startswith('$V '):
        input_str = message.content

        # Split the input string at '$VEGA', limiting the split to one occurrence
        split_str = input_str.split("$V", 1)

        # Check if the split was successful and store the second part in a new variable
        if len(split_str) > 1:
            command_args = split_str[1]
            print(f"The command arguments are: {command_args}")
            API.gptCall(command_args)
            await message.channel.send(API.contentOutput)



# if __name__ == '__main__':
#     # Start a new thread to handle command line input
#     input_thread = threading.Thread(target=handle_input)
#     input_thread.start()

client.run(TOKEN)
