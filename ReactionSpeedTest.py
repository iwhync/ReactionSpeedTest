import random
import pygame
import winsound

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Create a circle and a rectangle
circle_x, circle_y = 50, 550
circle_radius = 20
circle_color = (255, 0, 0)
rect_x = random.randint(1,800)
rect_y = random.randint(1,600)
rect_width, rect_height = 100, 75
rect_color = (0, 255, 0)
prev_rect_x = 0
prev_rect_y = 0

# Initialize variables for keeping score and game over status
high_score = 0
score = 0
game_over = False

FPS = 60
clock = pygame.time.Clock()

# Initialize time for rectangle
rect_time = pygame.time.get_ticks()

# Create rect objects for the circle and the rectangle
circle_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, 2*circle_radius, 2*circle_radius)
rect_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_over = True

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                running = False

        # Handle user input for moving
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            circle_y -= 15
        if keys[pygame.K_RIGHT]:
            circle_x += 15
        if keys[pygame.K_DOWN]:
            circle_y += 15
        if keys[pygame.K_LEFT]:
            circle_x -= 15

        # Update the rect objects for the circle and the rectangle
        circle_rect.x = circle_x - circle_radius
        circle_rect.y = circle_y - circle_radius
        rect_rect.x = rect_x
        rect_rect.y = rect_y

        # Check if the circle has not landed on the rectangle and reset your score
        if rect_x != prev_rect_x or rect_y != prev_rect_y:
            if not circle_rect.colliderect(pygame.Rect(prev_rect_x, prev_rect_y, rect_width, rect_height)):
                score = 0
                winsound.Beep(400, 200)
            rect_time = pygame.time.get_ticks()
            
    # Check if the circle has landed on the rectangle
        prev_rect_x = rect_x
        prev_rect_y = rect_y
        
        if circle_rect.colliderect(rect_rect):
            score += 1
            winsound.Beep(700, 10)
            rect_time = pygame.time.get_ticks()
            rect_x = random.randint(0, 700)
            rect_rect.x = rect_x
            rect_y = random.randint(0, 400)
            rect_rect.y = rect_y
            rect_time = pygame.time.get_ticks()

        # Check if the rectangle time has passed 1 sec and move the rectangle
        current_time = pygame.time.get_ticks()
        if current_time - rect_time > 1000:
            rect_y = random.randint(1,500)
            rect_x = random.randint(1,500)
            rect_rect.y = rect_y
            rect_rect.x = rect_x
            rect_time = pygame.time.get_ticks()

        # Draw the circle and rectangle on the screen
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
        pygame.draw.rect(screen, rect_color, (rect_rect.x, rect_rect.y, rect_width, rect_height))

        # Update the display
        high_score_font = pygame.font.Font(None, 30)
        high_score_text = high_score_font.render("High Score: " + str(high_score), 1, (255, 255, 255))
        screen.blit(high_score_text, (650, 40))
        score_font = pygame.font.Font(None, 30)
        score_text = score_font.render("Score: " + str(score), 1, (255, 255, 255))
        screen.blit(score_text, (650, 10))
        pygame.display.update()
        clock.tick(FPS)
        
        if score > high_score:
            high_score = score

# Quit pygame
pygame.quit()
