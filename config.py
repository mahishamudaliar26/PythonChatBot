# config.py
import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenent")
    
    AZURE_OPENAI_API_KEY = ""
    AZURE_OPENAI_API_ENDPOINT = "https://azureopenaiatqoeteamintegration.openai.azure.com/"
    AZURE_OPENAI_MODEL = "gpt-35-turbo"
    AZURE_OPENAI_API_VERSION = "2024-02-15-preview"