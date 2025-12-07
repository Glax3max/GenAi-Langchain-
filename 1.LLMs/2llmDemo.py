from langchain_anthropic import AnthropicLLM
from dotenv import load_dotenv

load_dotenv()

model = AnthropicLLM(model='claude-3-5-sonnet-20241022')

result  = model.invoke("What is the cpital of india")

print(result)