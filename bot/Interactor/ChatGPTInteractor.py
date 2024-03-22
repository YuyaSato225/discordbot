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
            model="ft:gpt-3.5-turbo-0125:personal::957qmUbl",
            messages=[
                {"role": "system", "content": "あなたはつくよみちゃんです。"},
                {"role": "user", "content": request.request},
            ],
        )
        print(response.choices[0].message.content)
        response = ChatGPTResponse(response=response.choices[0].message.content)
        return response


