import sys
try:
    age = int(input("年齢を入力してください！"))
except:
    print("数値を入力してください！")
    sys.exit()
else:
    if age >= 18:
        print("青年です")
    else:
        print("未成年です")
