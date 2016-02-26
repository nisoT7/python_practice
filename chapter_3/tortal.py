
# -*- encoding:utf8 -*-

##
# floatで計算する場合は初期化宣言は0.0
# int型は0
# 文字列は""
# で宣言する

total1 = 0.0
total2 = 0.0
num_total = 0
s = '1.23,2.43,3.123'
number = s.split(',')

##
# for文変数は格納される変数
# シーケンス部は要素数
# A2がCのような書き方要素数を数え配列に対応する要素にアクセスし足し算する
# A1はnumberに格納されている要素を変数に代入する形？

## A1
for i in number:
    total1 += float(i)
print total1

## A2
for i in range(len(number)):
    total2 += float(number[i])
print total2
