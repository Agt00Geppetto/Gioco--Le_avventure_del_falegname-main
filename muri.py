import arcade
import random

class Muri:

    def __init__(self, scene):
        
        self.scene = scene
        self.crea_muri()

    def crea_muri(self):
        # Barile
        barile = arcade.Sprite("./assets/barile.png")
        barile.center_x = random.randint(50, 10000)
        barile.center_y = 200
        barile.scale = 0.75
        self.scene.add_sprite("Walls", barile)

        # Secchio
        secchio = arcade.Sprite("./assets/secchio.png")
        secchio.center_x = random.randint(50, 10000)
        secchio.center_y = 170
        secchio.scale = 0.5
        self.scene.add_sprite("Walls", secchio)

        # Terreno
        for x in range(-1000, 10000, 1000):
            terreno = arcade.Sprite("./assets/terreno.png")
            terreno.center_x = x
            terreno.center_y = 75
            terreno.scale = 1.75
            self.scene.add_sprite("Walls", terreno)


        # Portone (limite x, y)
        for y in range(285, 10000, 100):
            for x in range(-10000, 20, 65):
                portone = arcade.Sprite("./assets/portone.png")
                portone.center_y = y
                portone.center_x = x
                portone.scale = 1.5
                self.scene.add_sprite("Walls", portone)