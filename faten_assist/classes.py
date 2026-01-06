import os
print(os.getenv("OPENAI_API_KEY"))
#this is just for testing!
class APIconfig:
    def __init__(self,api_key,model="gpt-4",max_tokens=1000):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")
        self.model=model
        self.max_tokens=max_tokens
        self.base_url="https://api.openai.com/v1/responses"