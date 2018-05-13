import sys
import json
from split_ip_address_from_cidr import split_ip_address_from_cidr
from join_this_split import join_this_split
from validate_ip_address_and_cidr import validate_ip_address_and_cidr
from print_network_class import print_network_class
from dec_to_bin_split import dec_to_bin_split
from get_dotted_mask_split import get_dotted_mask_split
from get_network_split_bin import get_network_split
from bin_to_dec_split import bin_to_dec_split
from get_first_host_split import get_first_host_split_bin
from get_last_host_split import get_last_host_split_bin
from get_number_of_hosts import get_number_of_hosts


def main():
    ip_address_dec = sys.argv[1]  # Otrzymany adres IP i CIDR
    # ip_address_dec = "192.168.45.171/9"
    ip_address_split_dec = []  # Lista dla adresu IP w formacie DEC
    mask_cidr = []  # Lista dla CIDR

    ###
    ###
    # Rozdzielanie
    split_ip_address_from_cidr(ip_address_dec, ip_address_split_dec, mask_cidr)  # Odzielenie IP od CIDR
    ip_address_split_bin = dec_to_bin_split(ip_address_split_dec)  # IP(dec) -> IP(bin)
    mask_cidr = mask_cidr[0]  # Przypisanie odzielonego CIDR z listy do "pojedynczej" zmiennej
    ip_address_dec = join_this_split(ip_address_split_dec)  # Do wyświetlania
    ip_address_bin = join_this_split(ip_address_split_bin)  # Do wyświetlania

    validate_ip_address_and_cidr(ip_address_split_dec, mask_cidr)  # Sprawdzenie poprawności IP i CIDR

    # Adres sieci
    network_split_bin = get_network_split(ip_address_split_bin, mask_cidr)
    network_split_dec = bin_to_dec_split(network_split_bin)
    network_bin = join_this_split(network_split_bin)
    network_dec = join_this_split(network_split_dec)

    # Maska podsieci
    subnet_mask_split_dec = get_dotted_mask_split(mask_cidr)  # Uzyskanie kropkowanej maski podsieci w formacie DEC
    subnet_mask_split_bin = dec_to_bin_split(subnet_mask_split_dec)  # -//- BIN
    subnet_mask_dec = join_this_split(subnet_mask_split_dec)  # Do wyświetlania
    subnet_mask_bin = join_this_split(subnet_mask_split_bin)  # Do wyświetlania

    # Fisrt Host
    first_host_split_bin = get_first_host_split_bin(network_split_bin, mask_cidr)
    first_host_split_dec = bin_to_dec_split(first_host_split_bin)
    first_host_bin = join_this_split(first_host_split_bin)
    first_host_dec = join_this_split(first_host_split_dec)

    # Last Host
    last_host_split_bin = get_last_host_split_bin(network_split_bin, mask_cidr)
    last_host_split_dec = bin_to_dec_split(last_host_split_bin)
    last_host_bin = join_this_split(last_host_split_bin)
    last_host_dec = join_this_split(last_host_split_dec)

    # Maksymalna ilość hostów
    number_of_hosts_dec = get_number_of_hosts(mask_cidr)
    number_of_hosts_bin = int(format(number_of_hosts_dec, '0b'))

    # Wyświetlenie
    print("###")
    print("IP (dec): ", ip_address_dec, sep='')
    print("IP (bin): ", ip_address_bin, sep='')
    print("Network (dec): ", network_dec, sep='')
    print("Network (bin): ", network_bin, sep='')
    network_class = print_network_class(network_split_bin)
    print("CIDR: /", mask_cidr, sep='')
    print("Subnet mask (dec): ", subnet_mask_dec, sep='')
    print("Subnet mask (bin): ", subnet_mask_bin, sep='')
    print("First Host (dec): ", first_host_dec, sep='')
    print("Fisrt Host (bin): ", first_host_bin, sep='')
    print("Last Host (dec): ", last_host_dec, sep='')
    print("Last Host (bin): ", last_host_bin, sep='')
    print("Number of Hosts (dec): ", number_of_hosts_dec, sep='')
    print("Number of Hosts (bin): ", number_of_hosts_bin, sep='')
    print("###")

    # Zapisanie do JSON
    data = {}
    data['ip_address'] = []
    data['ip_address'].append({
        'IP (dec)': ip_address_dec,
        'IP (bin': ip_address_bin,
        'Network (dec)': network_dec,
        'Network (bin)': network_bin,
        'Network Class': network_class,
        'CIDR': int(mask_cidr),
        'Subnet mask (dec)': subnet_mask_dec,
        'Subnet mask (bin)': subnet_mask_bin,
        'First Host (dec)': first_host_dec,
        'Fisrt Host (bin)': first_host_bin,
        'Last Host (dec)': last_host_dec,
        'Last Host (bin)': last_host_bin,
        'Number of Hosts (dec)': number_of_hosts_dec,
        'Number of Hosts (bin)': number_of_hosts_bin,
    })

    with open('ip_address.json', 'w') as outfile:
        json.dump(data, outfile)
        print(">>> Saved to JSON file <<<")


if __name__ == "__main__":
    main()
