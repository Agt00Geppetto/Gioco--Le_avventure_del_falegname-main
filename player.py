import arcade
import os
import random

class Player(arcade.Sprite):

    def __init__(self, texture_path, scale=1):
        super().__init__(texture_path, scale)

        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None
        base_path = "C:\\Users\\gabriele.bonaventura\\Desktop\\Gioco--Le_avventure_del_falegname-main-main\\assets\\spritesheets"

#Stato iniziale del giocatore (cioè fermo)
        self.state = "idle"
        
        self.textures_idle = [
            arcade.load_texture(f"{base_path}/idle/idle1.jpg"),
            arcade.load_texture(f"{base_path}/idle/idle2.jpg"),
            arcade.load_texture(f"{base_path}/idle/idle3.jpg"),
            arcade.load_texture(f"{base_path}/idle/idle4.jpg")
        ]
        self.textures_walk = [
            arcade.load_texture(f"{base_path}/walk/walk1.jpg"),
            arcade.load_texture(f"{base_path}/walk/walk2.jpg"),
            arcade.load_texture(f"{base_path}/walk/walk3.jpg"),
            arcade.load_texture(f"{base_path}/walk/walk4.jpg"),
            arcade.load_texture(f"{base_path}/walk/walk5.jpg"),
            arcade.load_texture(f"{base_path}/walk/walk6.jpg")
        ]
        self.textures_jump = [
            arcade.load_texture(f"{base_path}/jump/jump1.jpg"),
            arcade.load_texture(f"{base_path}/jump/jump2.jpg"),
            arcade.load_texture(f"{base_path}/jump/jump3.jpg"),
            arcade.load_texture(f"{base_path}/jump/jump4.jpg"),
            arcade.load_texture(f"{base_path}/jump/jump5.jpg"),
            arcade.load_texture(f"{base_path}/jump/jump6.jpg")
        ]
        self.textures_attack = [
            arcade.load_texture(f"{base_path}/attacco/attacco1.jpg"),
            arcade.load_texture(f"{base_path}/attacco/attacco2.jpg"),
            arcade.load_texture(f"{base_path}/attacco/attacco3.jpg"),
            arcade.load_texture(f"{base_path}/attacco/attacco4.jpg"),
            arcade.load_texture(f"{base_path}/attacco/attacco5.jpg"),
            arcade.load_texture(f"{base_path}/attacco/attacco6.jpg")
        ]
        self.textures_dead = [
            arcade.load_texture(f"{base_path}/dead/morte1.jpg"),
            arcade.load_texture(f"{base_path}/dead/morte2.jpg"),
            arcade.load_texture(f"{base_path}/dead/morte3.jpg"),
            arcade.load_texture(f"{base_path}/dead/morte4.jpg"),
            arcade.load_texture(f"{base_path}/dead/morte5.jpg"),
            arcade.load_texture(f"{base_path}/dead/morte6.jpg")
        ]
        self.textures_hurt = [
            arcade.load_texture(f"{base_path}/danno/danno1.jpg"),
            arcade.load_texture(f"{base_path}/danno/danno2.jpg"),
            arcade.load_texture(f"{base_path}/danno/danno3.jpg")
        ]
        self.textures_run = [
            arcade.load_texture(f"{base_path}/run/run1.jpg"),
            arcade.load_texture(f"{base_path}/run/run2.jpg"),
            arcade.load_texture(f"{base_path}/run/run3.jpg"),
            arcade.load_texture(f"{base_path}/run/run4.jpg"),
            arcade.load_texture(f"{base_path}/run/run5.jpg"),
            arcade.load_texture(f"{base_path}/run/run6.jpg")
        ]

#Indice che tiene conto di ogni frame dell'immagine
        self.cur_texture_index = 0

#Variabile che imposta la prima visione del personaggio come fermo
        #self.texture = self.textures_idle[0]

#Direzione verso la quale è rivolto il personaggioa alla'vvio del gioco
        self.direzione = 0 # 0 = destra; 1 = sinistra

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