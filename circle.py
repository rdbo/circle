import sys
import pygame
import math

def draw_circle(screen : pygame.Surface, center : tuple, radius : float, thickness : int, color : tuple):
	vertex_count = 100 * int(radius)
	angle_mod = 360.0 / vertex_count
	angle = 0.0
	old_point = (-1.0, -1.0)
	for i in range(0, vertex_count):
		dist_cos = (math.cos(angle / 180.0 * math.pi) * radius)
		dist_sin = (math.sin(angle / 180.0 * math.pi) * radius)
		new_point = (center[0] + dist_cos, center[1] + dist_sin)
		if old_point[0] == -1.0 and old_point[1] == -1.0:
			old_point = new_point
		pygame.draw.line(screen, color, old_point, new_point, thickness)
		old_point = new_point
		angle += angle_mod

def main():
	screen = pygame.display.set_mode((640, 480))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill((25, 25, 125))
		draw_circle(screen, (320, 240), 100.0, 2, (255, 0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	main()