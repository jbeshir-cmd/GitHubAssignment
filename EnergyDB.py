import sqlite3

class EnergyDB:
    """
    Stores energy data in memory using SQLite. Can read from a CSV and get totals.

    Attributes:
    conn (sqlite3.Connection): A connection to the SQLite in-memory database.
    """

    def __init__(self, filename):
        """
        Defines and creates the EnergyDB object by connecting to an in-memory database 
        and reading in data from the given CSV file.

        Args:
            filename (str): The path to the CSV file containing energy data.
        """
        self.conn = sqlite3.connect(":memory")
        self.read(filename)
    def __del__(self):
        """Clean up the database connection. 
        Closes the connection as well."""
        try:
            self.conn.close()
        except:
            pass
    def read(self, filename):
        """
        Reads data from the CSV file and inserts it into the database.

        Args:
            filename (str): The path to the CSV file containing energy data.
        
        Creates a table, and interest rows from the energy file
        """
        cursor = self.conn.cursor()
        cursor.execute(
        '''CREATE TABLE production 
        (year integer, state text, source 
        text, mwh real)''')

        try:
            with open(filename, 'r') as f:
                next(f)
                for line in f:
                    parts = line.strip().split(",")
                    if len (parts) != 4:
                        continue
                    try:
                        year = int(parts[0])
                        state = parts[1]
                        source = parts [2]
                        mwh = float(parts [3])
                    except ValueError:
                        continue

                    cursor.execute('INSERT INTO production VALUES (?,?,?,?)', (year, state, source, mwh))
        except FileNotFoundError:
            print(f"File not found: {filename}")

        self.conn.commit()
        

    def production_by_source(self, source, year):
        """
        Gets the total energy made by a certain source in a certain year.

        Args:
        source (str): The type of energy source (e.g., "Wind", "Solar").
        year (int): The year to filter energy production data.

        Returns:
        total(float): The total megawatt-hours of energy produced from the specified source and year.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT mwh FROM production WHERE source=? AND year=?", (source, year))
        rows = cursor.fetchall()
        total = 0
        for row in rows:
            total += row[0]
        return total
