def split_ip_address_from_cidr(ip_address, ip_address_split, mask_cidr):
    ip_address_split_temp = ip_address.split('.')
    ip_address_split_cidr_temp = ip_address_split_temp[3].split('/')
    mask_cidr.append(ip_address_split_cidr_temp[1])

    for i in range(0, 4):
        if i != 3:
            ip_address_split.append(ip_address_split_temp[i])
        else:
            ip_address_split.append(ip_address_split_cidr_temp[0])
