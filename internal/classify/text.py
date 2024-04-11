from openai import OpenAI

from ..config import config

client = OpenAI(
    api_key=config["OPEN_API_KEY"]
)

DEFAULT_TEMPERATURE = 0
DEFAULT_MAX_TOKENS = 500
DEFAULT_MODEL = "gpt-3.5-turbo"

class Prompt:
    def __init__(self, text_input, model: str = DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE):
        self.text_input = text_input
        # TODO handle role class types
        self.messages = [
            {"role": "user", "content": self.text_input}
        ]
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        
    def get(self):
        resp = client.completions.create(
            model=self.model,
            prompt=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        # TODO flatten choice response objects
        return resp.choices