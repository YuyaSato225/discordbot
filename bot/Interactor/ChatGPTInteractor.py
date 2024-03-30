import openai
import time
from .. import config
from ..Dtos.ChatGPTRequest import ChatGPTRequest
from ..Dtos.ChatGPTResponse import ChatGPTResponse
from ..Usecases.ChatGPTUsecase import ChatGPTUsecase

# インターフェース、ChatGPTUsecaseの実装
class ChatGPTInteractor(ChatGPTUsecase):
    def __init__(self):
        pass

    # ファインチューニングしたChatGPTと会話する関数
    def send_request(self, request: ChatGPTRequest) -> ChatGPTResponse:
        # api_keyを定義
        openai.api_key = config.OPENAI_API_KEY
        # ファインチューニングを行ったモデルにリクエストを送信
        response = openai.chat.completions.create(
            model="ft:gpt-3.5-turbo-0125:personal::957qmUbl",
            messages=[
                {"role": "system", "content": "あなたはつくよみちゃんです。"},
                {"role": "user", "content": request.request},
            ],
        )
        # 結果をDTOで返す
        print(response.choices[0].message.content)
        response = ChatGPTResponse(response=response.choices[0].message.content)
        return response

    # wikipediaを学習させたアシスタントと会話する関数
    def ask_ffx(self, request: ChatGPTRequest) -> ChatGPTResponse:
        # api_keyを定義して新規クライアントを作成
        client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        # 空の thread を作成する
        thread = client.beta.threads.create()
        # thread にユーザーからのメッセージを追加する
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request.request
        )
        # Run を作成する
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id="asst_8NdpCXSrMCxLQ4jY0l7vTu8e",
        )

        # Run のステータスが`completed`になるまで待つ
        while not run.status == "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            time.sleep(0.5)
            print(run.status)

        # Thread 上の message のリストを降順で取得する
        print("Thread")
        messages = client.beta.threads.messages.list(
            thread_id=thread.id,
            order="desc"
        )

        # Assistant によって追加された 内容を取得する
        assistant_messages = []
        for thread_message in messages.data:
            role = thread_message.role
            if role == "assistant":
                for content in thread_message.content:
                    content = content.text.value
                    assistant_messages.append(content)
            break
        # Assistantによって追加された最新のメッセージをDTOにして返す
        return ChatGPTResponse(response=assistant_messages[0])



