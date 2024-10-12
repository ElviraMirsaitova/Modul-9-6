def all_variants(text : str):
    for perebor_stroki in range(len(text)):
        for nacalo in range(len(text) - perebor_stroki):
            yield text[nacalo:nacalo + perebor_stroki + 1]

a = all_variants("abc")
for i in a:
    print(i)
