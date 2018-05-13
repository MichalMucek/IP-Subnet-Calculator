def get_number_of_hosts(mask_cidr):
    return pow(2, 32 - int(mask_cidr)) - 2
