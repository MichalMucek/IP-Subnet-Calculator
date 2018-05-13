import re


def validate_ip_address_and_cidr(ip_address_split, ip_address_mask):

    if len(ip_address_split) != 4:
        print("IP is not valid! -> exit(1)")
        exit(1)

    ip_pattern = re.compile(r"\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b")
    mask_pattern = re.compile(r"\b([0-9]|[12][0-9]|3[0-2])\b")

    for i in range(0, 4):
        if not ip_pattern.match(ip_address_split[i]):
            print("IP is not valid! -> exit(1)")
            exit(1)

        if i == 3:
            print("IP is valid! :)")

    if not mask_pattern.match(ip_address_mask):
        print("Mask is not valid! -> exit(1)")
        exit(1)
    else:
        print("Mask is valid! :)")
