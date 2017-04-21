import pygame
from random import *
pygame.init
black= (0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
def main():
	done=False
	window(1440,900)
	x=50
	y=50
	changex=0
	changey=0
	while done==False:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				print ("The user asked to quit")
				done=True
			elif event.type==pygame.KEYDOWN:
					if event.key==pygame.K_a:
						changex=-3
					elif event.key==pygame.K_d:
						changex=3
					elif event.key==pygame.K_s:
						changey=3
					elif event.key==pygame.K_w:
						changey=-3
			elif event.type==pygame.KEYUP:
				changey=0
				changex=0
			elif event.type==pygame.MOUSEBUTTONDOWN:
				print ("The user clicked down on the mouse")
		if changex!=0 or changey!=0:
			x=x+changex
			y=y+changey
		rectangle(x,y,changex,changey)
def window(x,y):
	size=(x,y)
	global screen
	screen=pygame.display.set_mode(size)
	pygame.display.set_caption("Game")
	screen.fill(white)
	pygame.display.flip()
def rectangle(x,y,changex,changey):
	if changex==3 and changey==0:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x-3,y,3,50],0)
		pygame.draw.rect(screen,white, [x,y-1,50,2],0)
		pygame.display.flip()
	elif changex==0 and changey==3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x-1,y,1,50],0)
		pygame.draw.rect(screen,white, [x,y-3,50,3],0)
		pygame.display.flip()
	elif changex==-3 and changey==0:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x+53,y,3,50],0)
		pygame.draw.rect(screen,white, [x,y-1,50,1],0)
		pygame.display.flip()
	elif changex==0 and changey==-3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x-1,y,1,50],0)
		pygame.draw.rect(screen,white, [x,y+53,50,3],0)
		pygame.display.flip()
	elif changex==3 and changey==-3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x+53,y,3,50],0)
		pygame.draw.rect(screen,white, [x,y+53,50,1],0)
		pygame.display.flip()
	elif changex==3 and changey==3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x-1,y,1,50],0)
		pygame.draw.rect(screen,white, [x,y-3,50,3],0)
		pygame.display.flip()
	elif changex==-3 and changey==-3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x+53,y,3,50],0)
		pygame.draw.rect(screen,white, [x,y-1,50,1],0)
		pygame.display.flip()
	elif changex==3 and changey==-3:
		pygame.draw.rect(screen, black, [x,y,50,50],0)
		pygame.draw.rect(screen,white, [x-1,y,1,50],0)
		pygame.draw.rect(screen,white, [x,y+53,50,3],0)
		pygame.display.flip()

main()
