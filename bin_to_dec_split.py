def bin_to_dec_split(bin_split):
    dec_split = []

    for i in range(0, 4):
        p = int(bin_split[i], 2)
        dec_split.append(str(p))

    return dec_split
