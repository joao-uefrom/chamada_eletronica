import re
import uuid


def get_mac_address():
    return ':'.join(re.findall('..', '%012X' % uuid.getnode()))
