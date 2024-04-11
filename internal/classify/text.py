import openai
from ..config import config

openai.api_key = config["OPEN_API_KEY"]

DEFAULT_TEMPERATURE = 0
DEFAULT_MAX_TOKENS = 500
DEFAULT_MODEL = "gpt-3.5-turbo"

class Prompt:
    def __init__(self, prompt, model: str = DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE):
        self.prompt = prompt
        # TODO handle role class types
        self.messages = [
            {"role": "user", "content": self.prompt}
        ]
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        
    def get(self):
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        # TODO flatten choice response objects
        return resp.choices