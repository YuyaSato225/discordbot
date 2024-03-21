from injector import Injector
from .Usecases.ChatGPTUsecase import ChatGPTUsecase
from .Interactor.ChatGPTInteractor import ChatGPTInteractor

class dependency:

    def __init__(self) -> None:
        # 依存関係を設定する関数を読み込む
        self.injector = Injector(self.__class__.config)

    # 依存関係を設定するメソッド
    @classmethod
    def config(cls, binder):
       # 抽象クラスをインスタンス化する際に具象クラスを使うよう登録する
        binder.bind(ChatGPTUsecase, ChatGPTInteractor)

    # injector.get()に引数を渡すと依存関係を解決してインスタンスを生成する
    def resolve(self, cls):
        return self.injector.get(cls)