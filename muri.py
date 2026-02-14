import arcade
import random

class Muri:

    def __init__(self):
        # Lista muri
        self.lista_muri = arcade.SpriteList(use_spatial_hash=True)
        self.crea_muri()

    def crea_muri(self):
        # Barile
        barile = arcade.Sprite("./assets/barile.png")
        barile.center_x = random.randint(50, 10000)
        barile.center_y = 200
        barile.scale = 0.75
        self.lista_muri.append(barile)

        # Secchio
        secchio = arcade.Sprite("./assets/secchio.png")
        secchio.center_x = random.randint(50, 10000)
        secchio.center_y = 170
        secchio.scale = 0.5
        self.lista_muri.append(secchio)

        # Terreno
        for x in range(-100, 10000, 1000):
            terreno = arcade.Sprite("./assets/terreno.png")
            terreno.center_x = x
            terreno.center_y = 75
            terreno.scale = 1.75
            self.lista_muri.append(terreno)


        # Portone (limite x, y)
        for y in range(285, 10000, 65):
            for x in range(-10000, 20, 65):
                portone = arcade.Sprite("./assets/portone.png")
                portone.center_y = y
                portone.center_x = x
                portone.scale = 1.5
                self.lista_muri.append(portone)


    def draw(self):
        self.lista_muri.draw()