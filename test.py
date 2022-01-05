#incrementer le score sans superposition
# 
#pip install pygame
import pygame
import random

from pygame.constants import MOUSEBUTTONDOWN

#verifie si tous les modules sont chargés
pygame.init()

#creation ecran
ecran = pygame.display.set_mode((800,700))
pygame.display.set_caption("Jouez à Pierre, Feuille, Ciseaux !")

#affiche image
ecran.fill((255,255,255))
imagef = pygame.image.load("feuille.png")
ecran.blit(imagef, (50, 420))
imagec = pygame.image.load("ciseaux2.png")
ecran.blit(imagec, (600, 420))
imagep = pygame.image.load("pierre.png")
ecran.blit(imagep, (325, 420))
imagevs = pygame.image.load("vs.png")
ecran.blit(imagevs, (300, 70))

#style txt
font_style = pygame.font.SysFont("bahnschrift", 20)
text = (0, 0, 0)

#contenu txt
value = font_style.render("Choisissez un symbole pour jouer", True, text)
ecran.blit(value, [250, 350])

scorejoueur = 0
scoremachine = 0

def ScoreJoueur(scorejoueur):
    value = font_style.render("Joueur : " + str(scorejoueur), True, text)
    ecran.blit(value, [100, 0])

def ScoreMachine(scoremachine):
    value = font_style.render("Machine : " + str(scoremachine), True, text)
    ecran.blit(value, [600, 0])

def Resultat(resultat):
    value = font_style.render("Victoire : " + str(resultat), True, text)
    ecran.blit(value, [325, 300])



#boucle de jeu
loop = True
i= 0
while loop:

    for event in pygame.event.get():

    # event input clavier
        if event.type == pygame.QUIT:
            loop = False

        #action de click
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


            #affichage et actions des boutons symboles
            clickfeuille = pygame.Rect((50,420), (150, 150))
            clickpierre = pygame.Rect((325,400), (150, 150))
            clickciseaux = pygame.Rect((600,400), (150, 150))

            #associé le click du joueur à une valeur
            ChoixHumainFinal = ""
            if clickfeuille.collidepoint(pos):
                ecran.blit(imagef, (75, 90))
                ChoixHumainFinal = "feuille"

            if clickpierre.collidepoint(pos):
                ecran.blit(imagep, (75, 90))
                ChoixHumainFinal = "pierre"

            if clickciseaux.collidepoint(pos):
                ecran.blit(imagec, (75, 90))
                ChoixHumainFinal = "ciseaux"


            #random choice de la machine après le choix (clic) du joueur    
            ChoixMachine = ["ciseaux", "feuille", "pierre"]
            ChoixMachineFinal = random.choice(ChoixMachine)

            if ChoixMachineFinal == "ciseaux":
                ecran.blit(imagec, (575, 90))

            if ChoixMachineFinal == "feuille":
                ecran.blit(imagef, (575, 90))

            if ChoixMachineFinal == "pierre":
                ecran.blit(imagep, (575, 90))


            #regles et augmentation/affichage du score
            if ChoixMachineFinal == ChoixHumainFinal:
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("nul")

            if ChoixMachineFinal == "ciseaux" and ChoixHumainFinal == "pierre":
                scorejoueur = scorejoueur + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(100, 0, 100, 30))
                ScoreJoueur(scorejoueur)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("joueur")

            if ChoixMachineFinal == "feuille" and ChoixHumainFinal == "ciseaux":
                scorejoueur = scorejoueur + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(100, 0, 100, 30))
                ScoreJoueur(scorejoueur)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))               
                Resultat("joueur")
                
            if ChoixMachineFinal == "pierre" and ChoixHumainFinal == "feuille":
                scorejoueur = scorejoueur + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(100, 0, 100, 30))
                ScoreJoueur(scorejoueur)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("joueur")
            
            if ChoixMachineFinal == "ciseaux" and ChoixHumainFinal == "feuille":
                scoremachine = scoremachine + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(600, 0, 130, 30))
                ScoreMachine(scoremachine)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("machine")
               
            if ChoixMachineFinal == "feuille" and ChoixHumainFinal == "pierre":
                scoremachine = scoremachine + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(600, 0, 130, 30))
                ScoreMachine(scoremachine)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("machine")  
                
            if ChoixMachineFinal == "pierre" and ChoixHumainFinal == "ciseaux":
                scoremachine = scoremachine + 1
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(600, 0, 130, 30))
                ScoreMachine(scoremachine)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(325, 300, 200, 30))
                Resultat("machine")



            #affichage et actions des boutons restart et exit apres avoir jouer 1 fois
            restart_img = pygame.image.load("bouton_restart.png")
            ecran.blit(restart_img, (225, 620))
            exit_img = pygame.image.load("bouton_exit.png")
            ecran.blit(exit_img, (500, 620))

            clickrestart = pygame.Rect((225,620), (100, 40))
            clickexit = pygame.Rect((500,620), (100, 40))

            if clickrestart.collidepoint(pos):
                print('restart')

                scorejoueur = 0
                scoremachine = 0
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(100, 0, 100, 30))
                ScoreJoueur(scorejoueur)
                pygame.draw.rect(ecran, (255, 255, 255), pygame.Rect(600, 0, 130, 30))
                ScoreMachine(scoremachine)

            if clickexit.collidepoint(pos):
                print('exit')
                pygame.quit()
                quit()
    
    pygame.display.flip()

#vider le cache
pygame.quit()
