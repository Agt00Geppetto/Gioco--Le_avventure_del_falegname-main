import arcade
import os

class Player(arcade.Sprite):
    def __init__(self, scale = 0.5):
        # Non passiamo nessuna immagine singola a Sprite
        super().__init__(scale = scale)

        # Variabili per il movimento e i salti
        self.jump_since_ground = 0
        self.max_jumps = 2
        self.physics_engine = None

        # Stato iniziale
        self.state = "idle"        # idle, walk, jump, run, attack, hurt, dead
        self.direzione = 0         # 0 = destra, 1 = sinistra
        self.cur_texture_index = 0

        # Carichiamo tutte le animazioni
        self.load_textures()

        # Impostiamo la prima texture visibile
        self.texture = self.textures_idle[0]

    def load_textures(self):
        
        # Cartella base delle sprite 
        # Il comando"os.path.join" è un metodo che ho trovato con ChatGPT per facilitare al computer la ricerca dei file nel 
        # percorso, dopodichè per ogni lista di textures, sempre per abbreviare e "pulire" il codice, grazie a ChatGPT. mi 
        # sono fatto scrivere come se fosse un ciclo for, da quale immagine a quale immagine dovesse prendere le animazioni 
        # il percorso di ogni singola lista, altrimenti con il mio codice, solo con l'elenco delle liste, arrivavoa a circa 
        # 100 righe se non di più

        base_path = os.path.join("C:", "Users", "gabriele.bonaventura", "Desktop",
                                 "Gioco--Le_avventure_del_falegname-main-main", "assets", "spritesheets")

        # Idle
        self.textures_idle = [arcade.load_texture(os.path.join(base_path, "idle", f"idle{i}.png")) for i in range(1, 5)]
        self.textures_idle_flipped = [arcade.load_texture(os.path.join(base_path, "idle", f"idle{i}.png"), flipped_horizontally=True) for i in range(1, 5)]

        # Walk
        self.textures_walk = [arcade.load_texture(os.path.join(base_path, "walk", f"walk{i}.png")) for i in range(1, 7)]
        self.textures_walk_flipped = [arcade.load_texture(os.path.join(base_path, "walk", f"walk{i}.png"), flipped_horizontally=True) for i in range(1, 7)]

        # Jump
        self.textures_jump = [arcade.load_texture(os.path.join(base_path, "jump", f"jump{i}.png")) for i in range(1, 7)]
        self.textures_jump_flipped = [arcade.load_texture(os.path.join(base_path, "jump", f"jump{i}.png"), flipped_horizontally=True) for i in range(1, 7)]

        # Attack
        self.textures_attack = [arcade.load_texture(os.path.join(base_path, "attacco", f"attacco{i}.png")) for i in range(1, 7)]
        self.textures_attack_flipped = [arcade.load_texture(os.path.join(base_path, "attacco", f"attacco{i}.png"), flipped_horizontally=True) for i in range(1, 7)]

        # Dead
        self.textures_dead = [arcade.load_texture(os.path.join(base_path, "dead", f"morte{i}.png")) for i in range(1, 7)]
        self.textures_dead_flipped = [arcade.load_texture(os.path.join(base_path, "dead", f"morte{i}.png"), flipped_horizontally=True) for i in range(1, 7)]

        # Hurt
        self.textures_hurt = [arcade.load_texture(os.path.join(base_path, "danno", f"danno{i}.png")) for i in range(1, 4)]
        self.textures_hurt_flipped = [arcade.load_texture(os.path.join(base_path, "danno", f"danno{i}.png"), flipped_horizontally=True) for i in range(1, 4)]

        # Run
        self.textures_run = [arcade.load_texture(os.path.join(base_path, "run", f"run{i}.png")) for i in range(1, 7)]
        self.textures_run_flipped = [arcade.load_texture(os.path.join(base_path, "run", f"run{i}.png"), flipped_horizontally=True) for i in range(1, 7)]

        # Dizionario animazioni
        self.animations = {
            "idle": (self.textures_idle, self.textures_idle_flipped),
            "walk": (self.textures_walk, self.textures_walk_flipped),
            "jump": (self.textures_jump, self.textures_jump_flipped),
            "run": (self.textures_run, self.textures_run_flipped),
            "attack": (self.textures_attack, self.textures_attack_flipped),
            "hurt": (self.textures_hurt, self.textures_hurt_flipped),
            "dead": (self.textures_dead, self.textures_dead_flipped),
        }

    def update_animation(self, delta_time=1/60):
        # Scegli la texture corretta in base a stato e direzione
        textures = self.animations[self.state][self.direzione]

        # Avanza frame
        # Queste righe servono a gestire l’animazione del personaggio 
        # facendo scorrere le immagini in modo fluido e ciclico. 
        # La variabile self.cur_texture_index è un contatore che aumenta 
        # di uno ad ogni aggiornamento del gioco, e rappresenta il tempo 
        # che sta passando nell’animazione. In questo modo non cambiamo
        #  immagine immediatamente ad ogni frame, ma utilizziamo questo
        #  contatore per controllare quando è il momento giusto per 
        # passare alla figura successiva. La condizione if self.cur_texture_index >= len(textures) * 6 
        # serve a verificare se abbiamo raggiunto la fine dell’animazione: len(textures)
        #  indica quante immagini compongono l’animazione, mentre il numero 6 stabilisce
        #  per quanti aggiornamenti ogni immagine deve restare visibile.
        #  Quando il contatore supera questo valore totale, viene 
        # riportato a zero così l’animazione riparte dall’inizio 
        # creando un ciclo continuo. Successivamente, con frame = self.cur_texture_index // 6 
        # utilizziamo una divisione intera per determinare quale immagine 
        # mostrare in quel momento: dividendo per 6 facciamo in modo che 
        # ogni immagine rimanga visibile per sei aggiornamenti prima di 
        # passare alla successiva. Infine, con self.texture = textures[frame] 
        # assegniamo allo sprite l’immagine corretta in base al frame calcolato, 
        # permettendo così al personaggio di apparire animato sullo schermo.

        self.cur_texture_index += 1
        if self.cur_texture_index >= len(textures) * 6:  # moltiplichiamo per 6 per rallentare l'animazione
            self.cur_texture_index = 0

        frame = self.cur_texture_index // 6
        self.texture = textures[frame]

    # Metodi movimento
    def set_physics_engine(self, engine):
        self.physics_engine = engine

    def move_left(self):
        self.change_x = -5

    def run_left(self):
        self.change_x = -10

    def move_right(self):
        self.change_x = 5

    def run_right(self):
        self.change_x = 10

    def stop(self):
        self.change_x = 0

    def jump(self):
        if self.physics_engine and (self.physics_engine.can_jump() or self.jump_since_ground < self.max_jumps):
            self.physics_engine.jump(10)
            self.jump_since_ground += 1

    def update_jump_reset(self):
        if self.physics_engine and self.physics_engine.can_jump():
            self.jump_since_ground = 0
