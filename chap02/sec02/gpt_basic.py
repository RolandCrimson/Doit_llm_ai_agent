from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("../.env")

client = OpenAI()

# ② 
response = client.chat.completions.create(
  model="gpt-4o",
  temperature=0.1,  # ③
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "2022년 월드컵 우승팀은 어디야?"},
  ]		# ④
)

print(response)

print('----')	# ⑤
print(response.choices[0].message.content) 
