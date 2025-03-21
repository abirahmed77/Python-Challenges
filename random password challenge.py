import random
import string

def randPass(length):
    
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    dg = string.digits
    pt = string.punctuation
    
    pd = [random.choice(lc), random.choice(uc),random.choice(dg), random.choice(pt)]
    
    characters = lc + uc + dg + pt

    pd = pd + random.choices(characters, k = length - len(pd)) 
    random.shuffle(pd) 
    
    return "".join(pd)

pl = random.randint(6, 10)
pd = randPass(pl)

print(f"The Password is : {pd}")