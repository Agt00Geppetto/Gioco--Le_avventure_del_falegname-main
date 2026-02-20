import arcade
import os
import random
#from inventario import InventarioSuper
from player import Player
from muri import Muri
from nemici import Enemy
#from barra_vita import Barra

"""
class Item:
    def __init__(self, name, texture_path, quantity=1):
        self.name = name
        self.texture = arcade.load_texture(texture_path)
        self.quantity = quantity

class UIInventory(arcade.Window):
    def __init__ (self):
        super().__init__()
    pass
"""

class GameView(arcade.Window):
    #impaginazione globale
    WINDOW_WIDTH : int = 1280
    WINDOW_HEIGHT : int = 950

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True,)

        #sprites
        self.p1 = None
        self.e1 = None
        self.barile = None
        self.secchio = None

        #fisica del gioco (base)
        self.pyshics_engine = None
        self.scene = None
        
        self.setup()

    def setup(self):
        #metodo per riassumere tutte le Spritelist di arcade   
        #prinicpali sprites da far collidere col giocatore (oltre al giocatore stesso)     
        self.scene = arcade.Scene()

        self.camera_sprites = arcade.Camera2D()
        self.camera_background = arcade.Camera2D()
        
        self.p1 = Player("./assets/Geppetto.png", 0.5)
        self.p1.center_x = 100
        self.p1.center_y = 315
        self.scene.add_sprite("Player", self.p1)

        self.e1 = Enemy("./assets/Legnamorta.png", 0.8)
        self.e1.center_x = 8000
        self.e1.center_y = 350
        self.scene.add_sprite("Enemy", self.e1)

        self.muri = Muri(self.scene)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite = self.p1,
            walls = self.scene["Walls"],
            # platforms = self.lista_piattafforme,
            # ladders = self.lista_scale,
            gravity_constant = 1.5,
        )

        self.p1.set_physics_engine(self.physics_engine)
        self.e1.set_physics_engine(self.physics_engine)
        

        self.physics_engine.enable_multi_jump(1)
        

        self.background = arcade.load_texture("./assets/sfondoG3.png")

    def on_draw(self):
        self.clear()

        self.camera_background.use()
        arcade.draw_texture_rect(
            self.background,
            arcade.XYWH(self.p1.center_x, 
            GameView.WINDOW_HEIGHT/2,
            GameView.WINDOW_WIDTH, 
            GameView.WINDOW_HEIGHT)
            )

        self.camera_sprites.use()
        self.scene.draw()

        #self.draw_health_bar()

    def on_update(self, delta_time):
        self.scene.update(delta_time)
        self.physics_engine.update()

        x,y = self.p1.position
        self.camera_sprites.position = arcade.Vec2(x, y)

        self.camera_background.position = arcade.Vec2(x, y)

        self.p1.update_jump_reset()
        
    def on_key_press(self, tasto, modificatori):
        if tasto == arcade.key.SPACE:
            self.p1.jump()
        elif tasto in (arcade.key.A, arcade.key.LEFT):
            self.p1.move_left()
            if modificatori == arcade.key.MOD_SHIFT:
                self.p1.run(change_x = -10)
        elif tasto in (arcade.key.D, arcade.key.RIGHT):
            self.p1.move_right()
            if modificatori == arcade.key.MOD_SHIFT:
                self.p1.run()

    def on_key_release(self, tasto, modificatori):
        if tasto == arcade.key.SPACE:
            pass
        elif tasto in (arcade.key.A, arcade.key.D, arcade.key.RIGHT, arcade.key.LEFT):
            self.p1.stop()
        elif tasto == arcade.key.ESCAPE:
            self.setup()

def main():
    window = GameView(
        800, 800, "Il mio giochino"
    )
    #window.setup()
    arcade.run()


if __name__ == "__main__":
    main()