import psycopg2
from config import load_config


def fetch_one():

	config = load_config()
	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cur:
				cur.execute("SELECT vendor_id, vendor_name from vendors ORDER BY vendor_name")
				print("The number of vendors: ", cur.rowcount)
				row = cur.fetchone()
				while row is not None:
					print(row)
					row = cur.fetchone()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)


def fetch_all():

	config = load_config()
	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cur:
				cur.execute("SELECT vendor_id, vendor_name from vendors ORDER BY vendor_name")
				print("The number of vendors: ", cur.rowcount)
				rows = cur.fetchall()

				for row in rows:
					print(row)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)


def iter_row(cursor, size=10):
	while True:
		rows = cursor.fetchmany(size)
		if not rows:
			break
		for row in rows:
			yield row

def fetch_many():

	config = load_config()
	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cur:
				cur.execute("""
				SELECT part_name, vendor_name
				FROM parts
				INNER JOIN vendor_parts on vendor_parts.part_id = parts.part_id
				INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
				ORDER BY part_name;
				""")
				for row in iter_row(cur, 10):
					print(row)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)




if __name__ == '__main__':
	print("Fetching vendors using fetchone()")
	fetch_one()

	print("Fetching vendors using fetchall()")
	fetch_all()

	print("Fetching vendor parts using fetchmany()")
	fetch_many()
