class UsuarioEntity:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def to_dict(self):
        """Convierte la entidad en un diccionario para JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre
        }