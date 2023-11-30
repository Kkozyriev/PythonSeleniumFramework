

import os

def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://localhost:8888/'
    elif env.lower() == 'prod':
        return 'http://localhost:8888/'
    else:
        raise Exception (f"Unknown environment: {env}")


