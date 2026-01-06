class APIConfig:
    def __init__(self,api_key,model="gpt-3.5-turbo",max_tokens=1000):
        self.api_key=api_key
        self.model=model
        self.max_tokens=max_tokens
        self.base_url="https://api.openai.com/v1/responses"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000
        
# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)