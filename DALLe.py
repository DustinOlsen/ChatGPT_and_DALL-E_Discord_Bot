import openai
import os
import dotenv

apiKey = os.getenv("OPENAI_API_KEY")

class DALLe_Image_Bot:
    name = "DALL-E"

    def __init__(self):
        self.image_url = ""

    def dalleCall(self, prompt, count):
        imageOutput = openai.Image.create(
            prompt=prompt,
            n=count,
            size="1024x1024"
        )
        # print(imageOutput)
        self.image_url = imageOutput['data'][0]['url']
        # print(image_url)