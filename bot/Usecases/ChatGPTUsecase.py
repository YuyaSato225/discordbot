from abc import ABCMeta, abstractmethod
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse

# インターフェース
class ChatGPTUsecase(metaclass=ABCMeta):
    
    # ファインチューニングしたChatGPTと会話する関数
    @abstractmethod
    def send_request(self, request: ChatGPTRequest) -> ChatGPTResponse:
        raise NotImplementedError
    
    # wikipediaを学習させたAssistantと会話する関数
    @abstractmethod
    def ask_ffx(self, request: ChatGPTRequest) -> ChatGPTResponse:
        raise NotImplementedError
    
    @abstractmethod
    def conversion_chara(self, request: ChatGPTRequest) -> ChatGPTResponse:
        raise NotImplementedError

