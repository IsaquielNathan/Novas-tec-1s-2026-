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
        self.velocidade = 5

    def mover(self, teclas):
        # Limita o movimento às bordas da tela
        if teclas[pygame.K_LEFT] and self.rect.x > 0: self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.x < 750: self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.y > 0: self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.y < 550: self.rect.y += self.velocidade

class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3):
        super().__init__(x, y, 40, 40, (220, 250, 10))
        self.velocidade = velocidade

    def perseguir(self, alvo):
        """Move o inimigo em direção ao alvo (jogador)."""
        if self.rect.x < alvo.rect.x: self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x: self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y: self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y: self.rect.y -= self.velocidade

def desenhar_hud(tela, estado):
    """Desenha o HUD (Heads-Up Display) do jogo."""
    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    tela.blit(texto_pont, (10, 10))
    fonte = pygame.font.SysFont(None, 25)

    for i in range(estado["vidas"]):
        texto_para_exibir = str(i) # Converte o número para texto
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
jogador = Jogador(375, 275)
inimigos = [
    Inimigo(random.randint(0, 750), random.randint(0, 100), random.randint(2, 4)) 
    for _ in range(4)
]
estado = {"pontuacao": 0, "vidas": 5, "rodando": True}
timer_spawn = 0

while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)
    
    for ini in inimigos:
        ini.perseguir(jogador)
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            ini.rect.topleft = (random.randint(0, 750), 0)
            if estado["vidas"] <= 0:
                estado["rodando"] = False

    # Spawn de novos inimigos a cada 300 frames
    timer_spawn += 1
    if timer_spawn % 300 == 0:
        inimigos.append(Inimigo(random.randint(0, 750), 0))
        estado["pontuacao"] += 50

    estado["pontuacao"] += 1 # +1 ponto por frame sobrevivido

    # Renderizar
    TELA.fill((20, 20, 40))
    jogador.desenhar(TELA)
    
    for ini in inimigos:
        ini.desenhar(TELA)
        
    desenhar_hud(TELA, estado) # função definida anteriormente
    
    pygame.display.flip()
    CLOCK.tick(60)

# Fim de jogo
desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()