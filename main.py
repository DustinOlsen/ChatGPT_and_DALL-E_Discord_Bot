import os
import discord
import dotenv
import API
import DALLe

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()

intents.messages = True
intents.members = True
intents.guilds = True

under_construction = True

client = discord.Client(intents=intents)
GUILD = os.getenv('GUILD')

imageBot = DALLe.DALLe_Image_Bot()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    if under_construction:
        await client.change_presence(activity=discord.Game("Under Construction"))

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


    if message.content.startswith('$D '):
        input_str = message.content

        split_str = input_str.split("$D", 1)

        if len(split_str) > 1:
            command_args = split_str[1]
            print(f"DALL-E Prompt: {command_args}")

            imageBot.dalleCall(command_args)

            await message.channel.send(command_args)
            await message.channel.send(imageBot.image_url)

        else:
            print("'$D' not found in input string")

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

        else:
            print("'$V' not found in input string")


client.run(TOKEN)

