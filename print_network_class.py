def print_network_class(network_split_bin):
    print("Network Class: ", sep='', end='')

    if network_split_bin[0][0] == '0':
        print("A", sep='')
        return 'A'
    else:
        if network_split_bin[0][1] == '0':
            print("B", sep='')
            return 'B'
        else:
            if network_split_bin[0][2] == '0':
                print("C", sep='')
                return 'C'
            else:
                if network_split_bin[0][3] == '0':
                    print("D", sep='')
                    return 'D'
                else:
                    print("E", sep='')
                    return 'E'
