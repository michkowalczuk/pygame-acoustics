import pygame
import os
from environment import *


os.environ['SDL_VIDEO_CENTERED'] = '1'  # centers window, must be before pygame.init()!
pygame.init()  # initialize pygame

PARTICLES_PER_SOURCE = 40
REFLECTION_ORDER = 5
PARTICLE_SPEED = 5
PARTICLE_SIZE = 4  # reflection_order + 1
BACKGROUND_COLOR = Color("Black")
START_COLOR = Color("Violet")
END_COLOR = Color("Green")

# pygame stuff
display_info = pygame.display.Info()  # create a video display information object
screen_size = int(display_info.current_w * 0.9), int(display_info.current_h * 0.9)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Simple Acoustics')

# initialize font
# must be called after 'pygame.init()' to avoid 'Font not Initialized' error
font = pygame.font.SysFont("consolas", 20)
label = font.render("LMC - add source / CMC - clean screen / RMC - start animation", 1, Color("White"))


def main():
    # create environment
    env = Environment(screen_size,
                      BACKGROUND_COLOR,
                      START_COLOR,
                      END_COLOR,
                      REFLECTION_ORDER)

    env.add_source(200, 200)

    clock = pygame.time.Clock()
    running = True
    animation = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # LEFT=1
                env.add_source(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:  # CENTER=2
                env.clean()
                animation = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # RIGHT=3
                # from each source create sound molecules
                env.generate_particles(PARTICLE_SIZE, PARTICLE_SPEED, PARTICLES_PER_SOURCE)
                animation = True

        if animation:
            # moves, reflects, cleaning dead particles
            env.update()

        # draw elements on screen
        screen.fill(env.background_color)

        # render text
        screen.blit(label, (10, 10))
        for particle in env.particles:
            pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.size)
        for source in env.sources:
            pygame.draw.circle(screen, source.color, (int(source.x), int(source.y)), source.size)

        pygame.display.flip()
        clock.tick(100)

    pygame.quit()

if __name__ == '__main__':
    main()
