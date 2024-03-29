import os


def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'https://www.demoblaze.com'

    else:
        raise Exception(f'Unknown environment: {env}')