from particle import *
from tools import *
from pygame import Color
import math


class Environment(object):
    """ Defines the boundary of a simulation and its properties """
    def __init__(self, env_size, background_color, start_color, end_color, reflection_order):
        self.width = env_size[0]
        self.height = env_size[1]
        self.background_color = background_color
        self.reflection_order = reflection_order
        self.particles_per_source = 360
        self.sources = []
        self.particles = []
        self.source_size = 10
        self.source_color = Color("Red")
        self.graduated_colors = create_range_of_colors(
            start_color,
            end_color,
            self.reflection_order)

    def add_source(self, x, y):
        """Adds sources to environment"""
        self.sources.append(Particle(x, y, self.source_size, self.source_color))

    def generate_particles(self, size, speed, particles_per_source):
        """Generates particles from each source"""
        for source in self.sources:
            for n in range(self.particles_per_source):
                x = source.x
                y = source.y
                particle = Particle(x, y, size, self.graduated_colors[0])
                particle.speed = speed
                particle.angle = 2 * math.pi * float(n) / particles_per_source
                self.particles.append(particle)

    def clean(self):
        """Clean all sources and molecules"""
        self.sources = []
        self.particles = []

    def update(self):
        for particle in self.particles:
            particle.move()
            order = self.check_reflection(particle)
            if order > self.reflection_order:
                continue
            color_idx = particle.reflection
            particle.color = self.graduated_colors[color_idx]
        self.particles[:] = [x for x in self.particles if x.reflection <= self.reflection_order]

    def check_reflection(self, particle):
        """Check whether reflection occurs for current particle"""
        reflection_occured = 0
        if particle.x > self.width - particle.size:
            particle.x = 2 * (self.width - particle.size) - particle.x
            particle.angle = -particle.angle
            reflection_occured = 1
        elif particle.x < particle.size:
            particle.x = 2 * particle.size - particle.x
            particle.angle = -particle.angle
            reflection_occured = 1
        if particle.y > self.height - particle.size:
            particle.y = 2 * (self.height - particle.size) - particle.y
            particle.angle = math.pi - particle.angle
            reflection_occured = 1
        elif particle.y < particle.size:
            particle.y = 2 * particle.size - particle.y
            particle.angle = math.pi - particle.angle
            reflection_occured = 1

        if reflection_occured == 1:
            particle.reflection += 1

        return particle.reflection
