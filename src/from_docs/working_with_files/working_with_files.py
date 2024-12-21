


# `with` - will automatically close the file
with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)



with open('test.txt', 'a', encoding='utf-8') as f:
    data = f.write('Hello, World!')
    print(data)
