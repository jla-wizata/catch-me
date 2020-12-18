import pygame


pygame.init()
screen = pygame.display.set_mode((500, 400))
done = False
is_blue = True
x = 30
y = 30
img = pygame.image.load('man.png')

clock = pygame.time.Clock()

font = pygame.font.SysFont("segoeuiblack", 15)
player_name = font.render("Plaaaaaaaayer 1", True, (0, 128, 0))


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_blue = not is_blue

		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_z]:
			y -= 10
		if pressed[pygame.K_s]: 
			y += 10
		if pressed[pygame.K_q]: 
			x -= 10
		if pressed[pygame.K_d]: 
			x += 10

		screen.fill((0, 0, 0))
		if is_blue:
			color = (0, 128, 255)
		else:
			color = (255, 100, 0)
		# pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
		screen.blit(img, (x, y))
		screen.blit(player_name, (x + (img.get_width()//2) - (player_name.get_width()//2), y - player_name.get_height()))

		pygame.display.flip()
		clock.tick(60)

