import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Moderation.create(
    input="ı wanna kill all of them",
  )
response_dict = response.to_dict()
print(json.dumps(response_dict, indent=2))