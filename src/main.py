import pyautogui
import time

# 実行時間計測
start = time.time()

# ImageNotFoundException::指定の画像が見つからなかった場合、これが出るらしいが、
# None が返ってきた

# ベースをチェック
base = pyautogui.locateOnScreen("./img/base_marble.png")
print(base)
if base == None:
    print("ベースアイテムが見つかりません")
else:
    # ベースの中心座標を取る
    bx, by = pyautogui.center(base)
    print("ベースアイテム発見伝！")

    # ほしいmodを探す region=(x,y,width,height)
    mod = None
    i = 0
    while mod == None and i < 10000:
        mod = pyautogui.locateOnScreen("./img/CoE_all_fire_skill_2.png", region=(250,538,402,100), minSearchTime=1)
        # mod = pyautogui.locateOnScreen("./img/CoE_to_energy_shield.png", region=(250,538,402,100), minSearchTime=1)
        print(mod)

        if mod != None:
            print("breakします")
            break
        else: 
            print("clickします")
            pyautogui.click(bx, by)
        
        i = i + 1
        print(i)
    end = time.time()
    dur = end - start
    print("クラフト終了！ 経過時間:{:.1f}".format(dur) + " [sec]")
