from openai import OpenAI
import os

# 根据环境变量获取 openai key\n",
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key=deepseek_api_key
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "把下面的的英文翻译为中文，注意不要解释你生成的答案。最后在末尾添加你可爱的表情。"
        },
        {
            "role": "user",
            "content": " \
            \n\nNewton's First Law: An object will remain at rest or in uniform straight-line motion \
            unless acted upon by an external force that compels it to change this state. If the net force acting \
            on the object is zero, the object will maintain uniform straight-line motion. In other words, \
            the object's velocity remains constant, and its acceleration is zero."
        }
    ],
    temperature=1.3,
    stream=False,
    max_tokens=2048, 
)

print(completion.choices[0].message.content)

