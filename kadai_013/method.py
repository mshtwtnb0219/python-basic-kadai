#商品を購入して、消費税を加えた計算結果を返す関数
def cal(price ,tax):
    return price + (price * tax)

#価格が1000円　消費税が10%の場合
print (cal(1000,0.1))
