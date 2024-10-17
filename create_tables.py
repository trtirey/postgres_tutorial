import psycopg2
from config import load_config

def create_tables():
	commands = (
		"""
		CREATE TABLE IF NOT EXISTS vendors (
			vendor_id SERIAL PRIMARY KEY,
			vendor_name VARCHAR(255) NOT NULL
		)
		""",
		"""
		CREATE TABLE IF NOT EXISTS parts (
			part_id SERIAL PRIMARY KEY,
			part_name VARCHAR(255) NOT NULL
		)
		""",
		"""
		CREATE TABLE IF NOT EXISTS part_drawings (
			part_id INTEGER PRIMARY KEY,
			file_extension VARCHAR(5) NOT NULL,
			drawing_data BYTEA NOT NULL,
			FOREIGN KEY (part_id)
			REFERENCES parts (part_id)
			ON UPDATE CASCADE ON DELETE CASCADE
		)
		""",
		"""
		CREATE TABLE IF NOT EXISTS vendor_parts (
			vendor_id INTEGER NOT NULL,
			part_id INTEGER NOT NULL,
			PRIMARY KEY (vendor_id, part_id),
			FOREIGN KEY (vendor_id)
				REFERENCES vendors (vendor_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			FOREIGN KEY (part_id)
				REFERENCES parts (part_id)
				ON UPDATE CASCADE ON DELETE CASCADE
		)
		""")

	try:
		config = load_config()
		with psycopg2.connect(**config) as conn:
			with conn.cursor() as cur:
				for command in commands:
					cur.execute(command)
	except (psycopg2.DatabaseError, Exception) as error:
		print(error)

if __name__ == '__main__':
	create_tables()
