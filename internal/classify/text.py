from openai import OpenAI

from ..config import config

client = OpenAI(
    api_key=config["OPEN_API_KEY"]
)

DEFAULT_TEMPERATURE = 0
DEFAULT_MAX_TOKENS = 500
DEFAULT_MODEL = "gpt-3.5-turbo"

class Prompt:
    def __init__(self, text_input: str, model: str = DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE):
        self.text_input = text_input
        self.messages = [
            {"role": "system", "content": "You are a helpful who creates activity calendars for up to 31 days in specific locations that I will ask you for and return only the activities results in JSON format"},
            {"role": "user", "content": self.text_input}
        ]
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        
    def get(self):
        resp = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            response_format={"type": "json_object"}
        )
        return resp.choices