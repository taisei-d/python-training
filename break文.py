kens = ["Tottori","Shimane","END","Hiroshima","Okayama","Yamaguchi"]


for ken in kens:
    if ken == "END":
        print("Break LOOP")
        break
    print(ken)
else:
    print("End LOOP")
for ken in kens:
    print(ken)
else:
    print("End LOOP")
