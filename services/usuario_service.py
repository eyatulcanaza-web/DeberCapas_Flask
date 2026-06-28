from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def obtener_todos_los_usuarios(self):
        """Lógica de negocio para listar usuarios."""
        usuarios_entidad = self.usuario_repository.buscar_todos()
        return [usuario.to_dict() for usuario in usuarios_entidad]

    def obtener_usuario_por_id(self, usuario_id):
        """Lógica de negocio para obtener un usuario por ID."""
        usuario = self.usuario_repository.buscar_por_id(usuario_id)
        if not usuario:
            return None
        return usuario.to_dict()