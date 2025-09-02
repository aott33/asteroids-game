import pygame
from constants import *

class MenuSystem:
	def __init__(self):
		self.font_large = pygame.font.Font(None, 72)
		self.font_medium = pygame.font.Font(None, 48)
		self.font_small = pygame.font.Font(None,36)

	def draw_main_menu(self, screen):
		screen.fill("black")
		center_x = SCREEN_WIDTH // 2
		center_y = SCREEN_HEIGHT // 2

		title_text = self.font_large.render("ASTEROIDS", True, "white")
		title_rect = title_text.get_rect(center = (center_x, center_y - 100))
		screen.blit(title_text, title_rect)

		start_text = self.font_medium.render("Press ENTER to Start", True, "white")
		start_rect = start_text.get_rect(center = (center_x, center_y))
		screen.blit(start_text, start_rect)

		quit_text = self.font_medium.render("Press Q to Quit", True, "gray")
		quit_rect = quit_text.get_rect(center = (center_x, center_y + 50))
		screen.blit(quit_text, quit_rect)

	def draw_game_over(self, screen, timer, score=None):
		screen.fill("black")
		
		game_over_text = self.font_large.render("GAME OVER", True, "red")
		game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
		screen.blit(game_over_text, game_over_rect)
		
		if score is not None:
			score_text = self.font_medium.render(f"Final Score: {score}", True, "white")
			score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
			screen.blit(score_text, score_rect)
		
		seconds_left = int(timer) + 1
		timer_text = self.font_medium.render(f"Returning to Menu in {seconds_left}...", True, "white")
		timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
		screen.blit(timer_text, timer_rect)

		skip_text = self.font_small.render("Press SPACE to Skip", True, "gray")
		skip_rect = skip_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
		screen.blit(skip_text, skip_rect)
	
	def draw_pause_menu(self, screen):
		overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		overlay.set_alpha(128)
		overlay.fill("black")
		screen.blit(overlay, (0, 0))
		
		pause_text = self.font_large.render("PAUSED", True, "white")
		pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
		screen.blit(pause_text, pause_rect)
		
		resume_text = self.font_medium.render("Press P to Resume", True, "white")
		resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
		screen.blit(resume_text, resume_rect)
	
	def handle_menu_input(self, event, game_state):
		if event.type == pygame.KEYDOWN:
			if game_state == MENU:
				if event.key == pygame.K_RETURN:
					return PLAYING
				elif event.key == pygame.K_q:
					return "QUIT"
			
			elif game_state == GAME_OVER:
				if event.key == pygame.K_SPACE:
					return MENU
		
		return game_state
