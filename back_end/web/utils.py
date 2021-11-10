import re


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def get_mac_address(request):
    if 'x-mac-address' in request.headers:
        mac_address = request.headers['x-mac-address']
        mac_address = sanitize(mac_address)
    else:
        mac_address = ''

    return mac_address


def is_valid_cpf(cpf: str) -> bool:
    if not cpf.isdigit():
        cpf = ''.join(re.findall(r'\d', cpf))

    if len(cpf) != 11:
        return False
    else:
        if cpf == '00000000000' or \
                cpf == '11111111111' or \
                cpf == '22222222222' or \
                cpf == '33333333333' or \
                cpf == '44444444444' or \
                cpf == '55555555555' or \
                cpf == '66666666666' or \
                cpf == '77777777777' or \
                cpf == '88888888888' or \
                cpf == '99999999999':
            return False

    cpf = [int(x) for x in cpf]

    s = cpf[:9]

    for _ in range(2):
        res = []
        for i, a in enumerate(s):
            b = len(s) + 1 - i
            res.append(b * a)

        res = sum(res) % 11

        if res > 1:
            s.append(11 - res)
        else:
            s.append(0)

    return s == cpf[:]


def is_valid_mac_address(mac_address: str) -> bool:
    pattern = r'^([0-9A-Fa-f]{2}[:\-.]?){5}[0-9A-Fa-f]{2}$'
    return bool(re.match(pattern, mac_address))


def sanitize(string: str) -> str:
    for r in ['.', '-', ':']:
        string = string.replace(r, '')
    return string
