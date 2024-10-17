import psycopg2 as p2
from config import load_config

def add_part(part_name, vendor_list):

	insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"

	assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s,%s)"

	conn = None
	config = load_config()

	try:
		with p2.connect(**config) as conn:
			with conn.cursor() as cur:

				cur.execute(insert_part, (part_name,))

				row = cur.fetchone()
				if row:
					part_id = row[0]
				else:
					raise Exception('Could not get the part id')

				for vendor_id in vendor_list:
					cur.execute(assign_vendor, (vendor_id, part_id))


				conn.commit()

	except (Exception, p2.DatabaseError) as error:
		print(error)


if __name__ == '__main__':

	part_list = [('SIM Tray', (1, 2)),
    		('Speaker', (3, 4)),
    		('Vibrator', (5, 6)),
    		('Antenna', (6, 7)),
    		('Home Button', (1, 5)),
			('LTE Modem', (1, 5))
			]

	for part, vendor_list in part_list:
		add_part(part, vendor_list)
