kens = ["Tottori","Shimane","END","Hiroshima","Okayama","Yamaguchi", "Hyogo"]

for ken in kens:
    if ken == "END":
        print("Break LOOP")
        continue
    print(ken)
else:
    print("End LOOP")
