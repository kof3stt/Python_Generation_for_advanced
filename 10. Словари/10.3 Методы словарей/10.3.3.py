text = "footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff"
result = dict()
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
