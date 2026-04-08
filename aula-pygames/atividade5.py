import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivência")
CLOCK = pygame.time.Clock()

# Fontes para o HUD e Game Over
fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)

class EntidadeBase:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor 

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):
        return self.rect.colliderect(outra.rect)

class Jogador(EntidadeBase):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, (66, 10, 100))
        self.velocidade = 8

    def mover(self, teclas):
        # Limita o movimento às bordas da tela
        if teclas[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.velocidade

class Bala(EntidadeBase):
    def __init__(self, x, y, alvo_x, alvo_y):
        # Dimensões 10x10 para um projétil mais simétrico
        super().__init__(x, y, 10, 10, (255, 255, 0)) 
        self.velocidade = 12
        
        # Float para manter a precisão do movimento diagonal
        self.pos_x = float(x)
        self.pos_y = float(y)

        dx = alvo_x - x
        dy = alvo_y - y
        distancia = (dx**2 + dy**2) ** 0.5

        if distancia == 0:
            distancia = 1 
        self.vel_x = (dx / distancia) * self.velocidade
        self.vel_y = (dy / distancia) * self.velocidade

    def voar(self):
        # Atualiza a posição exata (float)
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        
        # Atualiza o rect do pygame (que arredonda para int automaticamente)
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

    def fora_da_tela(self):
        # A bala é destruída ao sair por qualquer um dos 4 cantos da tela
        return (self.rect.bottom < 0 or self.rect.top > 600 or 
                self.rect.right < 0 or self.rect.left > 800)
    
class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3):
        super().__init__(x, y, 40, 40, (220, 250, 10))
        self.velocidade = velocidade
        self.vida = 3

    def perseguir(self, alvo):
        """Move o inimigo em direção ao alvo (jogador)."""
        if self.rect.x < alvo.rect.x: self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x: self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y: self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y: self.rect.y -= self.velocidade
class InimigoRapido(Inimigo):
    def __init__(self, x, y, velocidade_base=2):
        super().__init__(x, y, velocidade_base * 2) 
        self.cor = (10, 250, 250)

class InimigoGigante(Inimigo):
    def __init__(self, x, y, velocidade_base=2):
        super().__init__(x, y, velocidade_base)
        self.rect.width = 80 
        self.rect.height = 80
        self.cor = (250, 150, 10)
        self.vida = 5


def desenhar_hud(tela, estado):
    """Desenha o HUD (Heads-Up Display) do jogo."""
    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    tela.blit(texto_pont, (10, 10))
    fonte = pygame.font.SysFont(None, 25)

    for i in range(estado["vidas"]):
        texto_para_exibir = str(i) 
        imagem_do_texto = fonte.render(texto_para_exibir, True, (255, 80, 80))
        tela.blit (imagem_do_texto, (730 - i*35,25)) 

        #pygame.draw.circle(tela, (255, 80, 80), (730 - i*35, 25), 12)

def desenhar_game_over(tela):
    """Exibe a tela de Game Over centralizada."""
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render("GAME OVER", True, (255, 60, 60))
    tela.blit(texto, texto.get_rect(center=(400, 300)))

# ==========================================
# Configuração inicial do Mini-Game
# ==========================================


config_niveis = {
    1: {"vel_inimigo": 2, "max_inimigos": 3},
    2: {"vel_inimigo": 3, "max_inimigos": 5},
    3: {"vel_inimigo": 5, "max_inimigos": 8}
}

jogador = Jogador(375, 275)
inimigos = []
balas = [] 

estado = {
    "pontuacao": 0, 
    "vidas": 5, 
    "rodando": True,
    "nivel": 1,
    "mensagem_nivel": "",
    "tempo_mensagem": 0
}
timer_spawn = 0

while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1: # Botão esquerdo do mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Cria uma bala saindo do jogador e indo para a direção do mouse
                nova_bala = Bala(jogador.rect.centerx, jogador.rect.centery, mouse_x, mouse_y)
                balas.append(nova_bala)

    # Lógica do Nível
    novo_nivel = (estado["pontuacao"] // 500) + 1
    if novo_nivel > estado["nivel"] and novo_nivel <= 3:
        estado["nivel"] = novo_nivel
        estado["mensagem_nivel"] = f"Avançou para o Nível {estado['nivel']}!"
        estado["tempo_mensagem"] = 120 

    vel_atual = config_niveis[estado["nivel"]]["vel_inimigo"]
    max_inimigos_atual = config_niveis[estado["nivel"]]["max_inimigos"]

    # Atualizar Jogador
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)
    
    # Atualizar Tiros 
    for b in balas[:]: 
        b.voar()
        if b.fora_da_tela():
            balas.remove(b)
            continue
            
        for ini in inimigos[:]:
            if b.colidiu_com(ini):
                ini.vida -= 1 
                if b in balas: balas.remove(b) 
                if ini.vida <= 0:
                    estado["pontuacao"] += 50
                    if ini in inimigos: inimigos.remove(ini) 
                break

    # Atualizar Inimigos
    for ini in inimigos[:]:
        ini.perseguir(jogador)
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            if ini in inimigos: inimigos.remove(ini)
            if estado["vidas"] <= 0:
                estado["rodando"] = False

    # Spawn de Inimigos Gigantes e rápidos
    timer_spawn += 1
    if timer_spawn % 100 == 0 and len(inimigos) < max_inimigos_atual:
        x_spawn = random.choice([-50, 850]) 
        y_spawn = random.randint(0, 600)
        
        tipo_sorteio = random.randint(1, 10)
        if tipo_sorteio <= 6:
            novo_inimigo = Inimigo(x_spawn, y_spawn, vel_atual)
        elif tipo_sorteio <= 8:
            novo_inimigo = InimigoRapido(x_spawn, y_spawn, vel_atual)
        else:
            novo_inimigo = InimigoGigante(x_spawn, y_spawn, vel_atual)
            
        inimigos.append(novo_inimigo)

    estado["pontuacao"] += 1 

    # Renderizar
    TELA.fill((20, 20, 40))
    jogador.desenhar(TELA)
    
    for b in balas:
        b.desenhar(TELA)
        
    for ini in inimigos:
        ini.desenhar(TELA)
        
    desenhar_hud(TELA, estado) 
    
    # Desenha o aviso de novo Level 
    if estado["tempo_mensagem"] > 0:
        texto_avanco = fonte_grande.render(estado["mensagem_nivel"], True, (255, 255, 100))
        TELA.blit(texto_avanco, texto_avanco.get_rect(center=(400, 150)))
        estado["tempo_mensagem"] -= 1

    pygame.display.flip()
    CLOCK.tick(60)

# Fim de jogo
desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()