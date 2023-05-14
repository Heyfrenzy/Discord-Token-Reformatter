token = open('tokens.txt', 'r').read().splitlines():
with open('tokens.txt', 'w') as f:
    for fulltoken in tokens:
        if ":" in fulltoken:
            token = fulltoken.split(':')[2]
            f.write(token + '\n')
        else:
            f.write(fulltoken + '\n')
