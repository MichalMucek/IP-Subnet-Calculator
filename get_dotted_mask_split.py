def get_dotted_mask_split(ip_address_mask_cidr):
    p = int(ip_address_mask_cidr)
    ip_address_mask_dotted_split = []

    for i in range(4):
        if p >= 0:
            if p - 8 >= 0:
                ip_address_mask_dotted_split.append('255')

                p -= 8
            else:
                byte = 256 - pow(2, 8 - p)
                byte_str = str(byte)

                ip_address_mask_dotted_split.append(byte_str)

                p -= 8
        else:
            ip_address_mask_dotted_split.append('0')

    return ip_address_mask_dotted_split
