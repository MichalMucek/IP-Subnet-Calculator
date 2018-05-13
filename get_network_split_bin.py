def get_network_split(ip_address_split_bin, mask_cidr,):
    network_split = ip_address_split_bin
    split_number = int(mask_cidr) // 8
    in_split_pos = int(mask_cidr) % 8
    replacing_split_part = ""

    start_split = split_number

    while start_split <= 3:
        for i in range(0, 8):
            if start_split == split_number:
                if i < in_split_pos:
                    replacing_split_part += network_split[start_split][i]
                else:
                    replacing_split_part += '0'
            else:
                replacing_split_part += '0'

        network_split[start_split] = replacing_split_part
        replacing_split_part = ""
        start_split += 1

    return network_split
