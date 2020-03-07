months = {"1","2","3","4","1"}
print(months)
for x in months:
    print(x)
list = [1,2,12,1,2,12,23,44]
sets = set(list)
print(sets)
sets.add(100)
print(sets)
sets.remove(1)
print(sets)
sets.clear()
print(sets)


"""
set関数：listの中のユニーク（重複しない）値のみが出力される．
print(kazu | kisuu)全集合
print(kazu & kisuu)両方にあるもの
print(kazu - kisuu)引き算，含まれないもの
print(kazu ^ kisuu)どちらか一方にだけ含まれるものの要素，チルダ
