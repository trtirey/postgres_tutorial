import psycopg2 as p2
from config import load_config


def add_part(part_name, vendor_name):
    config = load_config()
    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_part(%s,%s)', (part_name, vendor_name))

            conn.commit()
    
    except (Exception, p2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    add_part('OLED', 'LG')
