def all_variants(text):
    n = len(text)
    for k in range(1, n + 1):
        for j in range(n - k + 1):
            yield text[j:j + k]

a = all_variants("abc")
for i in a:
    print(i)