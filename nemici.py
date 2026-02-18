import arcade
import random

class Enemy(arcade.Sprite):

    def __init__(self, texture_path, scale=1):
        super().__init__(texture_path, scale)

        pass

    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def attacco(self):
        pass

    def morte(self):
        pass