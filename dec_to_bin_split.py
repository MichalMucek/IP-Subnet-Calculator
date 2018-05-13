def dec_to_bin_split(dec_split):
    bin_split = []

    for i in range(0, 4):
        p = int(dec_split[i])
        bin_split.append(format(p, '08b'))

    return bin_split
