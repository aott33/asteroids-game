import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        x_pos = self.position.x
        y_pos = self.position.y
        old_radius = self.radius
        old_velocity = self.velocity
        self.kill()

        if old_radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            
            velocity1 = old_velocity.rotate(angle)
            velocity2 = old_velocity.rotate(-1*angle)

            new_radius = old_radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(x_pos, y_pos, new_radius)
            asteroid2 = Asteroid(x_pos, y_pos, new_radius)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2
