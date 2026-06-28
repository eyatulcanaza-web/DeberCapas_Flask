from config.database import DatabaseConnection
from models.usuario_entity import UsuarioEntity

class UsuarioRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def buscar_todos(self):
        """Trae todos los registros de la tabla usuarios."""
        conexion = self.db.get_connection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT id, nombre FROM usuarios")
        datos = cursor.fetchall()
        
        # Mapeo de POO: Convertimos filas SQL en objetos Python
        usuarios = [UsuarioEntity(id=row[0], nombre=row[1]) for row in datos]
        
        cursor.close()
        conexion.close()
        return usuarios

    def buscar_por_id(self, usuario_id):
        """Trae un único registro filtrado por su ID."""
        conexion = self.db.get_connection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT id, nombre FROM usuarios WHERE id = %s", (usuario_id,))
        row = cursor.fetchone()
        
        usuario = None
        if row:
            usuario = UsuarioEntity(id=row[0], nombre=row[1])
            
        cursor.close()
        conexion.close()
        return usuario