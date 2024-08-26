def all_variants(text):
    for j in range(0, len(text)):
        for k in range(0, len(text) - j):
            yield text[k:k + j + 1]


a = all_variants("abc")
for i in a:
    print(i)
