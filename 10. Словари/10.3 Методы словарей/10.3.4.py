s = "orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley"
res = dict()
for i in s.split():
    res[i] = res.get(i, 0) + 1
maxi = 0
otv = ""
for i in res:
    if res[i] > maxi:
        maxi = res[i]
        otv = i
    elif res[i] == maxi:
        otv = min(i, otv)
print(otv)
