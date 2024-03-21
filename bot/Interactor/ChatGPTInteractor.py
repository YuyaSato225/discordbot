import openai
from .. import config
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse
from ..Usecases.ChatGPTUsecase import ChatGPTUsecase

class ChatGPTInteractor(ChatGPTUsecase):
    def __init__(self):
        pass
    def send_request(self, request: ChatGPTRequest) -> ChatGPTResponse:
        openai.api_key = config.OPENAI_API_KEY

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.request},
            ],
        )
        print(response.choices[0].message.content)
        response = ChatGPTResponse(response=response.choices[0].message.content)
        return response


