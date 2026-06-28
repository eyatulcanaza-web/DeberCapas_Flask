import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "database": "Curso_Flask2", 
            "user": "postgres",
            "password": "12345",
            "port": 5432
        }
        
    def get_connection(self):
        """Retorna una conexión nueva y activa a la base de datos."""
        return psycopg2.connect(**self.config)