def get_last_host_split_bin(network_split_bin, mask_cidr):
    last_host_split_bin = network_split_bin
    split_number = int(mask_cidr) // 8
    in_split_pos = int(mask_cidr) % 8
    replacing_split_part = ""

    start_split = split_number

    while start_split <= 3:
        for i in range(0, 8):
            if start_split == 3 and i == 7:
                replacing_split_part += '0'
            else:
                if start_split == split_number:
                    if i < in_split_pos:
                        replacing_split_part += network_split_bin[start_split][i]
                    else:
                        replacing_split_part += '1'
                else:
                    replacing_split_part += '1'

        last_host_split_bin[start_split] = replacing_split_part
        replacing_split_part = ""
        start_split += 1

    return last_host_split_bin
