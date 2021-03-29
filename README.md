# dream_arts_program
株式会社 Dream Arts 採用選考（コーディングテスト）用プログラム
# 概要
このプロジェクトは，アラビア数字を大数表記の漢数字に変換するプログラム(kanji2number.py)と，大数表記の漢数字をアラビア数字に変換するプログラム(number2kanji.py)，2つのプログラムをテストするプログラム(test.py)で構成される．

アラビア数字を大数表記の漢数字に変換するプログラムと大数表記の漢数字をアラビア数字に変換するプログラムについては，AWSを用いてWebAPIのサービスとして公開

# 使い方
## test

$ python3 test.py

There is no arguments.

## kanji2number.py

- AWS Lambda + AWS API Gateway

 例（壱拾弐万参千壱百四拾弐 → 123142）

<https://4vx92pyk25.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/壱拾弐万参千壱百四拾弐>
<!-- 
例 (壱京 → statusCode 204)

<https://4vx92pyk25.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/壱京>
-->
## number2kanji.py

- AWS Lambda + AWS API Gateway
 例（1071960 → 壱百七万壱千九百六拾）

<https://4vx92pyk25.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/1071960>
<!--
例 (-1 → statusCode 204)

<https://4vx92pyk25.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/-1>
-->
# 環境
- macOS Catalina var. 10.15.7
- Python 3.8.2
- safari 14.0.2
- Google Chrome 89.0.4389.90 ※UTF-8のみに対応（拡張機能必須）

# Note
文字化けが発生する場合は，文字コードをUTF-8に変更して実行してください．
# Author

# License
