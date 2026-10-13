import items
import moteur
import time

moteur.pygame.init()

joueur = pygame.Rect(pos[0], pos[1], 40, 70)
arme = pygame.Rect(0, 0, 40, 20)
laser = pygame.Rect(0, 0, 20, 10)

mechant = pygame.Rect(800, 490, 60, 60)

  if touche[pygame.K_q] and pos[0] > 0 :
    vel[0] = - acceleration
    diff = -40
  
  elif touche[pygame.K_d] and pos[0] < 760 :
    vel[0] = acceleration
    diff = 40
  
  else :
    vel[0] = 0

  for plat in platformes :
    if vivant and joueur.colliderect(plat) and vel[1] >= 0 :
        joueur.bottom = plat.top
        pos[1] = joueur.y
        vel[1] = 0
        au_sol = True

  pos[0] += vel[0]
  pos[1] += vel[1]
    
  if mechant_vivant and arme.colliderect(mechant) :
    mechant_vivant = False

  if mechant_vivant and joueur.colliderect(mechant) : 
    vivant = False
    temps_mort = time.time()

  if not vivant and time.time() >= temps_mort + 5 :
    vivant = True
    pos = [40, 40]
    vel = [0, 0]

  else :
    vel[1] += gravite * 0.05

  if not mechant_vivant :
    mechant.x = 800
    mechant_vivant = True

  joueur.x = pos[0]
  joueur.y = pos[1]



  if vivant :
    pygame.draw.rect(screen, BLEU, joueur)

  if mechant_vivant :
    pygame.draw.rect(screen, ROUGE, mechant)
    mechant.x -= 5

  for plat in platformes :
    if plat == sol :
      couleur = VERT
    else :
      couleur = MARRON

    pygame.draw.rect(screen, couleur, plat)

  if shoot :
    laser.x += 20 * direction_shoot
    
    pygame.draw.rect(screen, VERT_P, laser)
    
    if laser.colliderect(mechant) and mechant_vivant :
      shoot = False
      laser.y = 1000
      mechant_vivant = False

    if laser.x > 800 or laser.x < -20 :
      shoot = False
  
  if touche[pygame.K_i] :
    arme.x = pos[0] + diff
    arme.y = pos[1] + 25
    pygame.draw.rect(screen, VIOLET, arme)
  else :
    arme.y = 600
  
  if touche[pygame.K_o] and not shoot:
    laser.x = pos[0] + (20 if diff == 40 else -10)
    laser.y = pos[1] + 30
    direction_shoot = 1 if diff == 40 else -1
    shoot = True



pygame.quit()