from serial import Serial
from serial.tools import list_ports

from source.config import Config

READ_VERSION = b"\xA1\x3A\x10\xFF\x00\xA8\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x77"

def get_checksum(packet: bytes)->int:
    """Returns packet checksum

    Args:
        packet (bytes): _description_

    Raises:
        ValueError: _description_

    Returns:
        int: _description_
    """
    if len(packet) != 24:
        raise ValueError("Not a valid packet length!")
    element_sum = 0
    i = 1
    for element in packet[1:23]:
        print(f"{i}: {element:x}")
        i+=1
        element_sum+=element
    return (256-element_sum)%256

class FConIsPacket:
    """ F-con IS packet class"""
    pocket = [
        0xA1,   # 0     body id
        0x3A,   # 1     header
        0x10,   # 2     header
        0xFF,   # 3     sec iS body
        0x00,   # 4     zero
        0x0,    # 5     msb
        0x0,    # 6     lsb
        0x0,    # 7     [data]
        0x0,    # 8     |data|
        0x0,    # 9     |data|
        0x0,    # 10    |data|
        0x0,    # 11    |data|
        0x0,    # 12    |data|
        0x0,    # 13    |data|
        0x0,    # 14    |data|
        0x0,    # 15    |data|
        0x0,    # 16    |data|
        0x0,    # 17    |data|
        0x0,    # 18    |data|
        0x0,    # 19    |data|
        0x0,    # 20    |data|
        0x0,    # 21    |data|
        0x0,    # 22    |data|
        0x0,    # 23    [data]
        0x0     # 24    checksum
    ]

    def __init__(self):
        ...
        
    
        
    


def get_avaliable_ports() -> dict:
    """_summary_

    Returns:
        list: _description_
    """
    ports = list_ports.comports()
    keys = (str(comport) for comport in ports if "- n/a" not in str(comport))
    values = (comport for comport in ports if "- n/a" not in str(comport))
    result = dict(zip(keys, values))

    return result


def fcon_read(cmd: str) -> str:
    result = ''
    print(f"{cmd}")
    return result


def fis_version_get(com_port_name: str):
    sp = Serial(
        port=com_port_name,
        baudrate=Config.BAUDRATE,
        bytesize=Config.BYTESIZE,
        parity=Config.PARITY,
        stopbits=Config.STOPBITS,
        timeout=1
    )

    with sp as port:
        port.write(READ_VERSION)
        answer = port.read(Config.PACKET_SIZE)

    return answer
