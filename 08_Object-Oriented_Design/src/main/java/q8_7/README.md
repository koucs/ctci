## 問題

8.7 チャットサーバをどのように実装するか説明してください。特にバックエンドの部分クラスやメソッドの詳細を説明して下さい。また、設計時に最も難しいと思われる問題も挙げてください。


## 構成

1. User管理サービス
2. Friend関係管理サービス
3. Chat情報管理サービス

## チャットサーバを作る上での難しさ

User管理サービスでOnlineStatus管理する上のネットワーク切断などの考慮  
-> Clientとサーバ間でwebsocket/webRTCなどのネットワーク疎通を確認するプロトコルを用いる

Friend関係管理サービスのデータ一貫性  
-> サービスレベルによってDatabaseのLockを使用するなど

単一障害点を作成しないためには  
-> FailSafeなしくみを検討する（CircuitBreakerなど）

DOS攻撃の対応方法  
-> RateLimit/origin IP addressからのフィルタリング/Bot Detectサービス活用によるDOS検知

