from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from openai import AzureOpenAI
from config import DefaultConfig

CONFIG = DefaultConfig()

class MyBot(ActivityHandler):
    async def gpt_response(self, user_query):
        client = AzureOpenAI(
            azure_endpoint=CONFIG.AZURE_OPENAI_API_ENDPOINT,
            api_key=CONFIG.AZURE_OPENAI_API_KEY,
            api_version=CONFIG.AZURE_OPENAI_API_VERSION
        )
        message_text = [
            {"role": "system", "content": "You are an AI assistant that helps people find information."},
            {"role": "user", "content": user_query},
        ]
        completion = client.chat.completions.create(
            model=CONFIG.AZURE_OPENAI_MODEL,
            messages=message_text,
            temperature=0.7,
            max_tokens=4096,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return completion.choices[0].message.content if completion.choices else "Sorry, I couldn't generate a response."
        

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        user_query = turn_context.activity.text  #Extracts text sent by user
        gptResponse = await self.gpt_response(user_query)  # Calls the gpt response method
        return await turn_context.send_activity(
            MessageFactory.text(f"{gptResponse}")
        )
    
