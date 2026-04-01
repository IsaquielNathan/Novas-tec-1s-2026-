class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.__id = id_usuario
        self.__nome = nome
        self.__email = ""
        self.set_email(email)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def set_id(self, novo_id): self.__id = novo_id
    def set_nome(self, novo_nome): self.__nome = novo_nome
    
    def set_email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
        else:
            print("E-mail inválido")

class GerenciadorUsuarios:
    def __init__(self):
        self.lista_usuarios = []
        
    def adicionar_usuario(self, usuario):
        if usuario.get_email() == "":
            print(f"O usuário '{usuario.get_nome()}' não foi cadastrado")
        else:
            self.lista_usuarios.append(usuario)
            print(f"Usuário '{usuario.get_nome()}' adicionado")
        
    def remover_usuario_por_id(self, id_usuario):
        for usuario in self.lista_usuarios:
            if usuario.get_id() == id_usuario:
                self.lista_usuarios.remove(usuario)
                print(f"Usuário ID {id_usuario} removido")
                return 
        print(f"Erro: Usuário com ID {id_usuario} não encontrado.")
        
    def listar_usuarios(self):
        print("\nUsuarios")
        if not self.lista_usuarios:
            print("Nenhum usuário cadastrado no momento.")
        else:
            for u in self.lista_usuarios:
                print(f"ID: {u.get_id()} | Nome: {u.get_nome()} | E-mail: {u.get_email()}")

sistema = GerenciadorUsuarios()

user1 = Usuario(1, "Isaquiel Nathan", "isaquiel@gmail.com")
user2 = Usuario(2, "Natan Isaque", "natanhotmail.com")
user3 = Usuario(3, "Isaqueu Natael", "natael@gmail.com.br")

sistema.adicionar_usuario(user1)
sistema.adicionar_usuario(user2)
sistema.adicionar_usuario(user3)
sistema.listar_usuarios()
sistema.remover_usuario_por_id(3)
sistema.listar_usuarios()