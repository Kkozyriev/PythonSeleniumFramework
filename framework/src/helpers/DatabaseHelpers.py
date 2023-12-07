import pymysql
from framework.src.helpers.GeneralHelpers import get_database_credentials
from framework.src.configs.GeneralConfigs import GeneralConfigs


def read_from_db(sql):
    db_creds = get_database_credentials()

    # connect to database
    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'],
                                 user=db_creds['db_user'], password=db_creds['db_password'])
    # read from the database
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # return the result
    return db_data


def get_order_from_db_by_order_no(order_no):
    schema = GeneralConfigs.DATABASE_SCHEMA
    table_prefix = GeneralConfigs.DATABASE_TABLE_PREFIX

    sql = f"SELECT * FROM {schema}.{table_prefix}posts WHERE ID={order_no} AND post_type = 'shop_order_placehold';"

    db_order = read_from_db(sql)

    return db_order
