import pyodbc


class Database:
    """
    Database class to connect to my Azure SQL Database.
    ToDo - make this into a Singleton.
    """
    def __init__(self,
                 server,
                 database,
                 user,
                 password,
                 driver='{ODBC Driver 17 for SQL Server}'):
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.driver = driver
    def __repr__(self):
        return f"Database class with host {self.host}, user {self.user}, and password {self.password}"
    def connect(self):
        """Connect to the database using the provided parameters"""
        self.my_db = pyodbc.connect(
            server=self.server,
            database=self.database,
            user=self.user,
            password=self.password,
            driver=self.driver
        )
    def create_cursor(self):
        """
        Run this to essentially create a command line to enter sql query
        using execute_command() below
        """
        self.my_cursor = self.my_db.cursor()
    def execute_command(self, cmd):
        """
        Runs whatever SQL query you pass it
        """
        self.my_cursor.execute(cmd)
        self.my_cursor.commit()
    def close_connection(self):
        """Closes the database connection"""
        self.my_db.close()
        
        