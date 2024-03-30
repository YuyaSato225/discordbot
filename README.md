# これは何？
OpenAIのapiとdiscord.pyを用いたdiscord上で動作するbotです。
コマンドを入力するとChatGPTと会話できます。

# 機能一覧
現在3つのコマンドが実装されています。
- test: 「おはようございます！」と即座に返します。
- send_request: つくよみちゃんAI育成計画(https://tyc.rei-yumesaki.net/material/kaiwa-ai/#terms1)
でファインチューニングしたGPT-3.5と会話ができます。
- ask_ffx: wikipedia(https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%8A%E3%83%AB%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%B8%E3%83%BCX)
を与えたAssistant(GPT-4-turbo)と会話ができます。

# 導入方法
サーバーにbotを追加可能な権限を持った人が

にアクセスするとこのbotを追加することができます。

# 使用方法
返答を受け取りたいチャンネルで、以下のコマンドを入力してください。
- `/test` おはようございます！と返します。
- `/send_request`　追加で `message_text` の入力が必要です。
- `/ask_ffx`追加で `message_text` の入力が必要です。

# 意識した点
- 3層アーキテクチャを意識したコードの分離　:　アプリケーション層、ビジネスロジック層、データ層への適切な分離を行っています。
- dependencyライブラリを用いた依存性の逆転　:　pythonのライブラリであるdependencyを用い、DIを行っています。これにより、各層を疎結合にし、クリーンアーキテクチャを実現しています。
- ファインチューニング、RAGの適切な使用　:　会話の口調、パターンの変更にはファインチューニングを、ドメイン知識の追加にはRAGを用いています。

# 各フォルダの役割
- bot: 実際のbotが入っています
  - application: アプリケーション層のコードが格納されています。
  - Dtos:　アプリケーション層とユースケース層間で受け渡すデータの型の定義です。
  - Usecase: ユースケース層のインターフェースです。今回は抽象クラスで実装しています。
  - Interactor: ユースケースの、実際の実装が格納されています。
- fine-tuning: ファインチューニングに用いたnotebookを格納しています。 

# クレジット
当botの作成には、フリー素材キャラクター「つくよみちゃん」が無料公開している会話テキストデータセットを使用しています。

■つくよみちゃん会話AI育成計画
https://tyc.rei-yumesaki.net/material/kaiwa-ai/
© Rei Yumesaki
