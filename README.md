## poe_autocrafter
ぽえのクラフトを自動化する

## 感想
```
画像認識して〇〇する　で100%の精度を持つのはポンとできることではなかったという学びがあった
OCRapiを間に挟むとクソほど精度が上がったのはたぶんgoogleOCRの学習済AIが優秀だから　なるほどなあ
2000回alterをうって1回出現する確率のものを見逃さずに検出するためには1回1秒ほど探索するように調整する必要があった
さすがにそれだと人力でやるほうがいいし、マウスを利用してBAN回避する都合上PCが封印される
```
## 次やるなら
- VMからやる（BANされ率高め+リソースだいぶ食いそう）
- もっと精度と速度を保てるライブラリ探せたり
- OCRAPI 1日に100万リクエストぐらい無料になってくれんかな: 
- 自分で学習させる？　ちょっと興味が出てきた
