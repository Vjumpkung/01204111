#R U Lucky?
n = input()
s = 0
m11,m12,m21,m22,m31,m32,m41,m42,m51,m52,m61,m62 = '2','0','1','3','1','8','8','0','3','1','9','3'
if n[0] == '0' and n[1] == '8':
    for i in range(len(n)):
        s = s + int(n[i])
    if s % 13 == 0 and s < 56:
        print("Have bad luck.")
    else:
        print("Have good luck.")
elif n[0] == '0' and n[1] == '9':
    for i in range(len(n)):
        try:
            if n[i] in m11 and n[i+1] in m12:
                print("Have bad luck.")
                break
            elif n[i] in m21 and n[i+1] in m22:
                print("Have bad luck.")
                break
            elif n[i] in m31 and n[i+1] in m32:
                print("Have bad luck.")
                break
            elif n[i] in m41 and n[i+1] in m42:
                print("Have bad luck.")
                break
            elif n[i] in m51 and n[i+1] in m52:
                print("Have bad luck.")
                break
            elif n[i] in m61 and n[i+1] in m62:
                print("Have bad luck.")
                break
        except IndexError:
            print("Have good luck.")