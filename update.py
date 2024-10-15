import psycopg2
from config import load_config

def update_vendor(vendor_id, vendor_name):
	# update vendor name based on vendor id

	update_row_count = 0

	sql = """ UPDATE vendors
				SET vendor_name = %s
				WHERE vendor_id = %s"""

	config = load_config()

	try:
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cur:
				cur.execute(sql, (vendor_name, vendor_id))
				update_row_count = cur.rowcount

			conn.commit()
	except (Exception, psyopg2.DatabaseError) as error:
		print(error)
	finally:
		return update_row_count

if __name__ == '__main__':
	update_vendor(1, "3m Corp")
