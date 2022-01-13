
# data compression function

def compress(data):

    src = []
    for b in data:
        src.append(int(b))

    ind = 200
    pack = []
    i = 0
    while i < len(src):
        ln = 12
        found = False
        while not found and ln > 11:
            j = i - ln
            while j >= 0 and (i - j) < 100:
                if src[i:i + ln] == src[j:j + ln]:
                    pack.append(ind)
                    pack.append(ln)
                    pack.append(ind)
                    pack.append(i - j)
                    pack.append(ind)
                    i += ln
                    found = True
                    break
                j -= 1
            ln -= 1
        if not found:
            pack.append(src[i])
            i += 1

    return pack
