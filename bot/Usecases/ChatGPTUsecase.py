from abc import ABCMeta, abstractmethod
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse

# 抽象クラス
class ChatGPTUsecase(metaclass=ABCMeta):
    
    @abstractmethod
    def send_request(self, request: ChatGPTRequest) -> ChatGPTResponse:
        raise NotImplementedError

