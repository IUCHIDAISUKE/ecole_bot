# echole-bot

## Rule

機能ごとで module を分けること
ここには、message を送る以外のことは基本書かないようにすること！(バグチェックが容易になるはず)

## To-do

- [ ] 基本的な要素ごとで moduke にわける
- [ ] データ分析 platform 作成
- [ ] DB との連携、修正
- [ ] reaction stamp での挙動の判定(つまり追加、するしないとか)
- [ ] help ページの追加
- [ ] test

基本的に、マジックコマンドとして discord 上から操作が完結できるようにする。
つまり、DB への追加、修正はすべて bot との会話で完結できるようにする。
マジックコマンドかつ管理者以外は反応しないような設計にする。
