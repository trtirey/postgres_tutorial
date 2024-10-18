# this file was created to try to troubleshoot an issue with the filenaming in the output of the insert_binary_data.py file
import psycopg2 as p2
from config import load_config


def delete_parts_drawings():

    config = load_config()

    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM part_drawings")

            conn.commit()

    except (Exception, p2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    delete_parts_drawings()
