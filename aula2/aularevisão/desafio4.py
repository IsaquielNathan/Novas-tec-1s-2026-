class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.jogador_atual = "X"
        self.total_jogadas = 0

    def mostrar_tabuleiro(self):
        print("\n  0   1   2")
        for i in range(3):
            print(f"{i} {self.tabuleiro[i][0]} | {self.tabuleiro[i][1]} | {self.tabuleiro[i][2]}")

    def fazer_jogada(self, linha, coluna):
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Lugar invalido")
            return False
        if self.tabuleiro[linha][coluna] != " ":
            print("Lugar errado")
            return False

        self.tabuleiro[linha][coluna] = self.jogador_atual
        self.total_jogadas += 1
        if self.jogador_atual == "X":
            self.jogador_atual = "O"
        else:
            self.jogador_atual = "X"     
        return True

    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] and self.tabuleiro[i][0] != " ":
                return self.tabuleiro[i][0]
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] and self.tabuleiro[0][i] != " ":
                return self.tabuleiro[0][i]

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] != " ":
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] != " ":
            return self.tabuleiro[0][2]

        return None

    def jogar(self):
        print("Jogo da Velha")
        while True:
            self.mostrar_tabuleiro()
            print(f"Vez do: {self.jogador_atual}") 
            linha = int(input("Linha (0, 1 ou 2): "))
            coluna = int(input("Coluna (0, 1 ou 2): "))
            
            if self.fazer_jogada(linha, coluna):
                vencedor = self.verificar_vencedor()
                
                if vencedor != None:
                    self.mostrar_tabuleiro()
                    print(f"Acabou {vencedor} ganhou!")
                    break
                
                if self.total_jogadas == 9:
                    self.mostrar_tabuleiro()
                    print("Deu velha")
                    break

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()