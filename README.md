# mypkg
![test](https://github.com/Kome-cyber/mypkg/actions/workflows/test.yml/badge.svg)
  * このリポジトリは、ロボットシステム学の講義で学習した、ROS2のパッケージです。
  * リポジトリ内には、二つのROS2パッケージ
    * talker.py
    * listener.py
が存在します。
    
## 主な機能
  * talker.py
    * 0.5秒ずつ数値をカウントし、listener.pyに数値を送信します。
  * listener.py
    * talker.pyから送信された数値を表示します。
    
## 使用方法
```
#入力
$ ros2 launch mypkg talk_listen.launch.py

#出力
[listener-2] [INFO] [1672120473.510242700] [listener]: Listen: 0
[listener-2] [INFO] [1672120473.993824800] [listener]: Listen: 1
[listener-2] [INFO] [1672120474.493537400] [listener]: Listen: 2
[listener-2] [INFO] [1672120474.993829300] [listener]: Listen: 3
[listener-2] [INFO] [1672120475.494233800] [listener]: Listen: 4
[listener-2] [INFO] [1672120475.993709200] [listener]: Listen: 5
[listener-2] [INFO] [1672120476.493527600] [listener]: Listen: 6
．．．

```
## 動作確認済み環境
  * Ubuntu 22.04.1 LTS
  * Python 3.10

## ライセンス
 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
 * © 2022 Koumei Ainoya

