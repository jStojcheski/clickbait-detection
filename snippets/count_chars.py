def count_chars(series):
    charset = dict()
    
    for item in series:
        for char in set(item):
            if char not in charset.keys():
                charset[char] = 0
            charset[char] += 1
            
    print(len(charset), 'characters found.\n')
            
    return charset