import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gptCall(chatInput):
    global contentOutput

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chatInput}
        ]
    )
    print(completion.choices[0].message.content)
    contentOutput = completion.choices[0].message.content



