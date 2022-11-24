def get_all_tokens(filename:str): #returns all tokens in a file as token from email:password:token
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens

all_tokens = get_all_tokens("tokens.txt")
open("tokens.txt", "w").write("".join(all_tokens))
