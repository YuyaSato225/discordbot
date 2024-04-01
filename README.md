# これは何？
OpenAIのapiとdiscord.pyを用いたdiscord上で動作するbotです。
コマンドを入力するとChatGPTと会話できます。

# 機能一覧
現在3つのコマンドが実装されています。
- test: 「おはようございます！」と即座に返します。
- send_request: つくよみちゃんAI育成計画(https://tyc.rei-yumesaki.net/material/kaiwa-ai/#terms1)
でファインチューニングを行い、口調の変更をしたGPT-3.5-turboと会話ができます。
- ask_ffx: wikipedia(https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%8A%E3%83%AB%E3%83%95%E3%82%A1%E3%83%B3%E3%82%BF%E3%82%B8%E3%83%BCX)
を与え、このページの情報を取得したAssistant(GPT-4-turbo)と会話ができます。

# 導入方法

### 各自のbotで動かす場合
1. `config.py` の `DISCORD_BOT_TOKEN` に、自分のbotのdiscord bot tokenを入力してください。
2. `config.py` の `OPENAI_API_KEY` に入力するOpenAI api key は、別途連携します。
3. このリポジトリをダウンロードしたフォルダに移動し、 `pip install -r requirments.txt` を実行
4. `python3 -m bot.main` を実行

### 常時稼働しているbotを導入したい場合
導入するためのリンクを別途共有します。

# 使用方法
返答を受け取りたいチャンネルで、以下のコマンドを入力してください。
- `/test` おはようございます！と返します。
- `/send_request`　追加で `message_text` の入力が必要です。
- `/ask_ffx`追加で `message_text` の入力が必要です。

# 意識した点
- 3層アーキテクチャを意識したコードの分離　:　アプリケーション層(discordとのやり取りを担当)、ビジネスロジック層(OpenAI apiとのやり取りを担当)、データ層(現在該当する機能はなし)への適切な分離を行っています。
- dependencyライブラリを用いた依存性の逆転　:　pythonのライブラリであるdependencyを用い、DIを行っています。これにより、各層を疎結合にし、クリーンアーキテクチャを実現しています。
- ファインチューニング、RAGの適切な使用　:　会話の口調、パターンの変更にはファインチューニングを、ドメイン知識の追加にはRAGを用いています。

# 各フォルダの役割
- bot: 実際のbotが入っています
  - application: アプリケーション層のコードが格納されています。discordとのやり取りを担当します。
  - Dtos:　アプリケーション層とビジネスロジック層間で受け渡すデータ型(DTO)の定義です。
  - Usecase: ビジネスロジック層のインターフェースです。今回は抽象クラスで実装しています。OpenAI apiとのやり取りを担当します。
  - Interactor: ビジネスロジックの、実際の実装が格納されています。
- fine-tuning: ファインチューニングに用いたnotebookを格納しています。 

# 技術的詳細
アプリケーション層
- discordのbot部分はdiscord.py(https://pypi.org/project/discord.py/)
を使用しています。

ビジネスロジック層
- OpenAI apiの呼び出しには(https://pypi.org/project/openai/)
を使用しています。
- `/send_request` で用いているモデルのファインチューニングは、 `fine_tuning` 内にあるノートブックを用いています。
- `/ask_ffx` ではAssistant apiを呼び出しています。

デプロイ
- 常時稼働には、AWSのEC2を用いています。

# 今後の予定
1. RAGを自前のアーキテクチャで構築する
2. TRPGのルールブックとか学習させたい

# クレジット
当botの作成には、フリー素材キャラクター「つくよみちゃん」が無料公開している会話テキストデータセットを使用しています。

■つくよみちゃん会話AI育成計画
https://tyc.rei-yumesaki.net/material/kaiwa-ai/
© Rei Yumesaki
