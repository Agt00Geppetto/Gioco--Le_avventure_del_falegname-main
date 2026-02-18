import arcade
import os
import random

class Player(arcade.Sprite):

    def __init__(self, texture_path, scale=1):
        super().__init__(texture_path, scale)

        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

#Stato iniziale del giocatore (cioè fermo)
        self.state = "idle"
        
        self.textures_idle = []
        self.textures_walk = []
        self.textures_jump = []
        self.textures_attack = []
        self.textures_dead = []
        self.textures_hurt = []

#Indice che tiene conto di ogni frame dell'immagine
        self.cur_texture_index = 0

#Variabile che imposta la prima visione del personaggio come fermo
        self.texture = self.textures_idle[0]

#Chiaramente per "invocare" la funzione
        self.load_textures()

    def load_textures(self):
        pass

    def update_animation(self, delta_time = 1 / 60):
        pass

    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def move_left(self):
        self.change_x = -5

    def move_right(self):
        self.change_x = 5

    def run(self):
        self.change_x = 10

    def stop(self):
        self.change_x = 0

    def jump(self):
        if self.physics_engine and (
            self.physics_engine.can_jump()
            or self.jump_since_ground < self.max_jumps
        ):
            self.physics_engine.jump(10)
            self.jump_since_ground += 1

    def update_jump_reset(self):
        if self.physics_engine and self.physics_engine.can_jump():
            self.jump_since_ground = 0