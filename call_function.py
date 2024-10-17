import psycopg2 as p2
from config import load_config


def get_parts(vendor_id):
    
    parts = []

    config = load_config()
    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                #cur = conn.curcor() 
                # Note that get_parts_by_vendor is a user-defined function in the Postgres suppliers database
                cur.callproc('get_parts_by_vendor', [vendor_id,])

                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

    except (Exception, p2.DatabaseError) as error:
        print(error)
    finally:
        return parts
if __name__ == '__main__':
    parts = get_parts(1)
    print(parts)
