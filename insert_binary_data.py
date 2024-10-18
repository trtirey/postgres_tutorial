# Note that this a concatenated version of the code presented in the tutorial
import psycopg2 as p2
from config import load_config


def write_blob(part_id, path_to_file, file_extension):
    
    config = load_config()

    data = open(path_to_file, 'rb').read()

    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO part_drawings(part_id, file_extension, drawing_data) VALUES(%s,%s,%s)',
                    (part_id, file_extension, p2.Binary(data)))

            conn.commit()

    except (Exception, p2.DatabaseError) as error:
        print(error)


def read_blob(part_id, path_to_dir):

    config = load_config()

    try:
        with p2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(""" Select part_name, file_extension, drawing_data
                                FROM part_drawings
                                INNER JOIN parts on parts.part_id = part_drawings.part_id
                                WHERE parts.part_id = %s """,
                            (part_id,))

                blob = cur.fetchone()

                open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
    except (Exception, p2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    write_blob(1, 'images/input/simtray.png', 'png')
    write_blob(2, 'images/input/speaker.png', 'png')

    read_blob(1, 'images/output/')
    read_blob(2, 'images/output/')
