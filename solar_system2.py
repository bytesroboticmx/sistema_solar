import pygame
import math

# Inicializar pygame
pygame.init()

# Configuracion de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sistema solar completo")

# Define los colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
CYAN = (0, 255, 255)

# Define los parametros del sistema solar
sun_radius = 50
sun_pos = (width // 2, height // 2)

planet_data = [
    {"name": "Mercury", "color": GRAY, "radius": 10, "distance": 100, "speed": 0.03},
    {"name": "Venus", "color": ORANGE, "radius": 15, "distance": 130, "speed": 0.02},
    {"name": "Earth", "color": BLUE, "radius": 20, "distance": 160, "speed": 0.03},
    {"name": "Mars", "color": RED, "radius": 18, "distance": 190, "speed": 0.009},
    {"name": "Jupiter", "color": ORANGE, "radius": 35, "distance": 220, "speed": 0.005},
    {"name": "Saturn", "color": YELLOW, "radius": 30, "distance": 250, "speed": 0.004},
    {"name": "Uranus", "color": CYAN, "radius": 25, "distance": 280, "speed": 0.003},
    {"name": "Neptune", "color": BLUE, "radius": 23, "distance": 310, "speed": 0.002}
]

# Ciclo principal del sistema solar
running = True
while running:
    # Evento handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el fondo de pantalla
    screen.fill(BLACK)

    # Dibujar el sol
    pygame.draw.circle(screen, YELLOW, sun_pos, sun_radius)

    # Actualizar y dibujar cada planeta
    for planet in planet_data:
        planet_radius = planet["radius"]
        planet_distance = planet["distance"]
        planet_speed = planet["speed"]

        planet_angle = pygame.time.get_ticks() / 1000 * planet_speed
        planet_x = sun_pos[0] + planet_distance * math.cos(planet_angle)
        planet_y = sun_pos[1] + planet_distance * math.sin(planet_angle)

        pygame.draw.circle(screen, planet["color"], (int(planet_x), int(planet_y)), planet_radius)

         # Dibujar la orbitas con elipses
        orbit_width = planet_distance * 2
        orbit_height = planet_distance * 2
        orbit_rect = pygame.Rect(sun_pos[0] - planet_distance, sun_pos[1] - planet_distance, orbit_width, orbit_height)
        pygame.draw.ellipse(screen, planet["color"], orbit_rect, 1)

    # Actualiza la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()
