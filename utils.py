def generate_random_ip_address() -> str:
    from random import randint
    return f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'


