from sys import argv

from source.communication import get_avaliable_ports, fis_version_get, READ_VERSION

def main(**kwargs):
    """Emtry poin

    Returns:
        _type_: _description_
    """
    print(f"Loaded!")
    
    
    
    ports = get_avaliable_ports()
    print(f"{ports.keys()}")
    avaliable_ports_count = len(ports.keys())
    if avaliable_ports_count < 1:
        print("No active port found (")
        return 1
    port_num = int(input(f"Enter port number from 0 to {avaliable_ports_count-1}: "))
    port_name = str(list(ports.values())[port_num]).split(" ", maxsplit=1)[0]
    print(f"Great!\nYou'we chosen port {port_name}")
    
    a = fis_version_get(port_name)

    i = 0
    for c in zip(READ_VERSION, a):
        print(f"BYTE_{i}\t>\t{c[0]:x}\t-\t{c[1]:x}")
        i+=1
    
if __name__ == '__main__':
    main(argv=argv)