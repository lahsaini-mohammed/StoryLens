import base64
from groq import Groq
from app.config import LLAVA_MODEL, GROQ_API_KEY

class ImageProcessor:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def process_image(self, image_path):
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        prompt = f"Describe this image in detail, focusing on elements that could be part of a story:"
        response = self.client.chat.completions.create(
            model=LLAVA_MODEL,
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]}
            ]
        )
        return response.choices[0].message.content