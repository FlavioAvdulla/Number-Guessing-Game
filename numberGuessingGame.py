import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Colors
BACKGROUND = (25, 25, 40)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (95, 160, 210)
INPUT_BOX = (50, 80, 120)
HIGHLIGHT = (255, 215, 0)

# Fonts
title_font = pygame.font.SysFont("arial", 48, bold=True)
main_font = pygame.font.SysFont("arial", 32)
message_font = pygame.font.SysFont("arial", 28)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = BUTTON_COLOR
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=12)
        pygame.draw.rect(surface, TEXT_COLOR, self.rect, 2, border_radius=12)
        
        text_surface = main_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def is_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.color = BUTTON_HOVER
            return True
        self.color = BUTTON_COLOR
        return False
    
class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.unicode.isdigit() and len(self.text) < 3:
                    self.text += event.unicode
        return None
    
    def draw(self, surface):
        pygame.draw.rect(surface, INPUT_BOX, self.rect, border_radius=8)
        pygame.draw.rect(surface, TEXT_COLOR, self.rect, 2, border_radius=8)
        
        text_surface = main_font.render(self.text, True, TEXT_COLOR)
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))