def decompress(pack):

    write_pack = []
    unpack = []
    i = 0
    ind = 200

    while i < len(pack):
        if pack[i] == ind and pack[i + 2] == ind and pack[i + 4] == ind:
            ln = pack[i + 1]
            dist = pack[i + 3]
            if not unpack[-dist: -dist + ln]:
                x = 0
                while x != ln:
                    unpack.append(unpack[-dist])
                    x += 1
            else:
                unpack += unpack[-dist: -dist + ln]
            i += 5
            continue
        unpack.append(pack[i])
        i += 1

    for x in unpack:
        write_pack.append(x)

    return write_pack
