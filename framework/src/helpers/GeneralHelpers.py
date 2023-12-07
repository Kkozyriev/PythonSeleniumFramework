import os
from framework.src.configs.GeneralConfigs import GeneralConfigs


def get_base_url():
    # env = os.environ.get('ENV', 'local')
    env = GeneralConfigs.ENV

    if env.lower() == 'local':
        return GeneralConfigs.local_url
    elif env.lower() == 'prod':
        return GeneralConfigs.prod_url
    else:
        raise Exception(f"Unknown environment: {env}")


def get_database_credentials():
    # env = os.environ.get('ENV', 'local')
    # db_user = os.environ.get("DB_USER")
    # db_password = os.environ.get("DB_PASSWORD")
    # if not db_user or not db_password:
    #     raise Exception("Environment variables 'DB_USER and 'DB_PASSWORD' must be set.")
    env = GeneralConfigs.ENV

    if env == 'local':
        db_host = GeneralConfigs.local_host
        db_port = GeneralConfigs.local_port
    elif env == 'prod':
        db_host = GeneralConfigs.prod_host
        db_port = GeneralConfigs.prod_port
    else:
        raise Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}
    return db_info
