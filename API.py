import os
import openai
import dotenv


dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

testBot = True

conversation = [
    {"role": "system", "content": "Please respond as if you're VEGA, the sentient intelligence assigned to mars by the UAC"}
]


def gptCall(chatInput):
    global content_output
    global conversation

    # messages = conversation + [{"role": "user", "content": chatInput}]
    conversation.append({"role": "user", "content": chatInput})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    response = completion.choices[0].message.content
    print(response)

    content_output = completion.choices[0].message.content

    conversation.append({"role":"assistant", "content": response})
    content_output = response

    if testBot:
        with open("test_conversation.txt", "w") as file:
            for message in conversation:
                file.write(f"{message['role']}: {message['content']}\n")

    else:
        with open("conversation.txt", "w") as file:
            for message in conversation:
                file.write(f"{message['role']}: {message['content']}\n")