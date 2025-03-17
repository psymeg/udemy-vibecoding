import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penguin Fish Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Load assets
penguin_img = pygame.image.load("penguin.png")
penguin_img = pygame.transform.scale(penguin_img, (50, 50))
fish_img = pygame.image.load("fish.png")
fish_img = pygame.transform.scale(fish_img, (30, 30))

# Game variables
penguin = pygame.Rect(100, HEIGHT // 2, 50, 50)
penguin_size = 50
fish_list = []
SPEED = 5
score = 0
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and penguin.y > 0:
        penguin.y -= SPEED
    if keys[pygame.K_DOWN] and penguin.y < HEIGHT - penguin.height:
        penguin.y += SPEED
    
    # Generate fish
    if random.randint(1, 50) == 1:
        fish_list.append(pygame.Rect(WIDTH, random.randint(50, HEIGHT - 50), 30, 30))
    
    # Move fish and check collision
    for fish in fish_list[:]:
        fish.x -= SPEED
        screen.blit(fish_img, (fish.x, fish.y))
        if fish.colliderect(penguin):
            fish_list.remove(fish)
            if random.choice([True, False]):
                penguin_size += 5  # Grow
            else:
                penguin_size = max(30, penguin_size - 5)  # Shrink but not too small
            penguin.width = penguin_size
            penguin.height = penguin_size
            penguin_img_scaled = pygame.transform.scale(penguin_img, (penguin_size, penguin_size))
            score += 1
    
    # Draw penguin
    screen.blit(pygame.transform.scale(penguin_img, (penguin_size, penguin_size)), (penguin.x, penguin.y))
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

