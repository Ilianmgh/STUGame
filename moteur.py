import pygame
import items

couleurs = {
  "NOIR" : (20, 20, 20),
  "BLEU" : (20, 20, 255),
  "VIOLET" : (95, 40, 110),
  "VERT" : (20, 255, 20),
  "VERT_P" : (0, 255, 0),
  "GRIS" : (50, 50, 50),
  "ROUGE" : (255, 20, 20),
  "MARRON" : (180, 120, 40)
}
class Game :
  def __init__ (self) :
    pygame.init()

    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Platforme")

    self.gravite = 9.8

    self.clock = pygame.time.Clock()

    self.running = True

  def shows_sprite (self) :
    for item in items.item_list :
      pygame.draw.rect(self.screen, couleurs[item.color], item.plat)

    for car in items.character_list :
      if car.vivant :
        pygame.draw.rect(self.screen, couleurs[car.color], car.sprite)

  def gravity(self, car : items.Character):
    car.vel[1] += self.gravite * 0.05

  def all_movement (self) :
    for car in items.character_list :
      car.movement()

  def gaming (self) :
    sol = items.Sol ()
    platforme_1 = items.Platforme(40, 400)
    joueur = items.Player()

    while self.running :

      for event in pygame.event.get () :
        if event.type == pygame.QUIT :
          self.running = False
          
      touche = pygame.key.get_pressed()

      self.screen.fill(couleurs["NOIR"])

      self.gravity(joueur)
      self.all_movement()

      if touche[pygame.K_z] :
        joueur.jump()

      if touche[pygame.K_q] :
        joueur.move(-1)

      elif touche[pygame.K_d] :
        joueur.move(1)
      
      else :
        joueur.move(0)

      self.shows_sprite()

      pygame.display.flip()

      self.clock.tick(60)
    
    pygame.quit()

jeu = Game ()
jeu.gaming()