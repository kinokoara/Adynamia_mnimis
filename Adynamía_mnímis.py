import random

#神経衰弱用番号の設定用関数
def randomnumber():
    rnum = random.randint(1, 100)
    return rnum
#配列をコピーしてランダムに書き換えるための添字設定関数
def ypnumber():
    rnum = random.randint(0,7)
    return rnum

#神経衰弱の実際の値を比較して配列を操作する関数
def select(fs,ss,rootarray):

    print(f"選択した要素の数値は{rootarray[int(fs)]}と{rootarray[int(ss)]}だよ")

    #残りペア数カウント
    pairparameater = len(rootarray) / 2

    #2つの値が同じかの判定処理
    if rootarray[int(fs)] == rootarray[int(ss)]:
        delnum = rootarray[int(fs)]
        #配列要素からペアが成立した値を削除
        rootarray.remove(delnum)
        rootarray.remove(delnum)
        pairparameater -= 1

        print(f"ペア成立!残り{int(pairparameater)}ペア")

    else:
        print(f"ペア不成立!残り{int(pairparameater)}ペア")
    #返り血として編集した配列を返す
    return rootarray


# ランダムな整数8個格納用配列
mnimis1 = []
# 上記配列の順番を入れ替えて格納する配列
mnimis2 = []

# 二つの配列を合わせてゲーム用に使う配列
rootmnimis = []

# 8個配列の要素を剪定する
while(1):
    anum = randomnumber()
    # 8この中で値が被らないように判定する
    if anum in mnimis1:
        anum = randomnumber()
    else:mnimis1.append(str(anum))
    # 8個別の値が格納されたらループを終える
    if len(mnimis1) == 8:
        break

# ランダムに並び替えて配列に格納し直す
while(1):
    ypnum = ypnumber()
    if mnimis1[ypnum] in mnimis2:
        ypnum = ypnumber()
    else:mnimis2.append(str(mnimis1[ypnum]))
    if len(mnimis2) == 8:
        break


# 二つの配列を合わせる
rootmnimis = mnimis1 + mnimis2

print(rootmnimis)


i = 0
# 神経衰弱本体 20回まで挑戦できる
for i in range(21):
    # 20になるとおしまい
    if i == 20:
        print("gameover")
        break
    paramenon = len(rootmnimis) - 1
    fselect = int(input(f"1つ目：取り出したい番号を選んでね(0~{paramenon})"))
    sselect = int(input(f"2つ目：取り出したい番号を選んでね(0~{paramenon})"))
    # 同じところを選んだら挑戦回数を減らしてもう一度入力させる
    if fselect == sselect:
        print("同じ番号の入力は不正です。一回分回答権剥奪します")
        continue
    # 比較するために関数を呼び出す
    rootmnimis = select(fselect,sselect,rootmnimis)

    #更新された配列の要素が0個なら全てペアになったのでループ終了
    if len(rootmnimis) == 0:
        print(f"ゲーム終了{i + 1}回でクリア！")
        break
    # 配列の要素数が減っていたら減った要素分入力を促す範囲を狭める
    elif paramenon > len(rootmnimis):
        paramenon -= 2

        print(f"あと{19 - i}回!")
        i += 1
    else:
        print(f"あと{19 - i}回!")



