#
import psycopg2 as p2
from config import load_config


def delete_part(part_id):

    config = load_config()

    rows_deleted = 0
    sql = 'DELETE FROM parts WHERE part_id=%s'

    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (part_id,))
                rows_deleted = cur.rowcount

            conn.commit()

    except (Exception, p2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted


if __name__ == '__main__':
    deleted_rows = delete_part(4)
    print("Deleted Rows: ", deleted_rows)
