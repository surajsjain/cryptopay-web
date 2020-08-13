import random

def generate_key(name):
    nme = name.lower()
    otp = str(random.randint(1000, 9999))

    code = ''
    code = code + otp[:2]

    for n in nme:
        new_char = (ord(n)-97 + random.randint(0, 25)) % 25
        new_char += 97

        char_or_num = random.randint(0,1)

        if(char_or_num == 0):
            new_char_ch = chr(new_char)
            code += new_char_ch
        else:
            code += str(new_char)

    code += otp[2:]

    if(len(code)>30):
        code = code[:30]

    return code
