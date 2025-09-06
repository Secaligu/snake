import pygame, sys, random
from pygame.math import Vector2

pygame.init()
 
  #<|variables|>#
BG_COLOR = (156, 200, 255)
SNAKE_COLOR = (2, 74, 191)
SNAKE_FOOD = (2, 76, 204)

cell_size = 30
number_of_cell = 25

class Food:
    def __init__(self):
      self.position = self.generate_ramdom_pos()
    def draw(self):
        Food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, Food_rect)
        
    def generate_ramdom_pos(self):
      x = random.randint(0, number_of_cell - 1)
      y = random.randint(0, number_of_cell - 1)
      position = Vector2(x, y)
      return position

class Snake:
  def __init__(self):
    self.body = [Vector2(6, 9), Vector2(5,9), Vector2 (4,9)]
    self.direction = Vector2(1,0)
    self.add_segment = False
    
  def draw(self):
    for segment in self.body:
      segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
      pygame.draw.rect(screen, SNAKE_COLOR, segment_rect,0, 6)
      
  def update(self):
    self.body.insert(0, self.body[0] + self.direction)
    if self.add_segment == True:
      self.add_segment = False
    else:
      self.body.pop()
    
class Game:
  def __init__(self):
    self.snake = Snake()
    self.food = Food()
    
  def draw(self):
    self.snake.draw()
    self.food.draw()
    
  def update(self):
    self.snake.update()
    self.check_colision_with_food()
  
  def check_colision_with_food(self):
    if self.snake.body[0] == self.food.position:
      self.food.position = self.food.generate_ramdom_pos()
      self.snake.add_segment = True  

screen = pygame.display.set_mode((cell_size*number_of_cell, cell_size*number_of_cell ))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

game = Game()

food_surface = pygame.image.load("arandano.png")

SNAKE_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SNAKE_UPDATE, 125)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
          game.update()
          
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
           game.snake.direction = Vector2(0, -1)
          if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
           game.snake.direction = Vector2(0, 1)
          if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
           game.snake.direction = Vector2(-1, 0)
          if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
           game.snake.direction = Vector2(1, 0)
    
    screen.fill(BG_COLOR)       
    game.draw()
    
    pygame.display.update()
    clock.tick(60)        
 