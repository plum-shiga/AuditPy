# -*- coding: utf-8 -*-
'''
やりたいこと
===
input 2つのファイル
output サンプリングされたエクセル

2つのファイル
---
### ファイルA
1
2
3
### ファイルB
2
3
4

output
---
前期 当期 当期母集団 サンプリング
1 2
2 3
3 4 1 1

サンプリング（固定配列）
---
[1, 2, 5, 20, 25]
↑ 当期母集団の数に依存して自動判別される

'''

def irekae(list) -> int:
    return 0

# zenki: list[str] = []
# touki: list[str] = []
zenki = []
touki = []

print('aaaaaaa')

with open('./f1.txt', 'r') as f:
    zenki = f.readlines()
with open('./f2.txt', 'r') as f:
    touki = f.readlines()

print('zenki ===')
print(zenki)
print('touki ===')
print(touki)

print('irekae ===')
print(irekae(zenki))

