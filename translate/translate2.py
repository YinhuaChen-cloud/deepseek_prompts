import requests
import json
import os

# 根据环境变量获取 openai key\n",
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

# 替换为你自己的API密钥
api_key = deepseek_api_key
# DeepSeek API的请求URL
api_url = "https://api.deepseek.com/v1/chat/completions"

# 请求的头部信息，包含API密钥和指定请求内容类型为JSON
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 请求的数据，包含聊天消息（这里是翻译请求）和模型参数
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个专业的翻译助手，能够准确地将英文翻译成中文。"},
        {"role": "user", "content": "Translate the following English text to Chinese: 'Hello, world!'"}
    ],
    "temperature": 0.7, # 控制生成文本的随机性，值越大越随机，0.7是一个常用取值
    "max_tokens": 2048 # 最大生成的token数，可根据需求调整，这里设置为2048
}

# 发送POST请求到API端点
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# 检查响应状态码
if response.status_code == 200:
    result = response.json()
    # 提取翻译结果
    translation = result["choices"][0]["message"]["content"]
    print(f"翻译结果: {translation}")
else:
    print(f"请求失败，状态码: {response.status_code}，错误信息: {response.text}")
