@namespace
class SpriteKind:
    Shield = SpriteKind.create()
    RapidFire = SpriteKind.create()
    Invincibility = SpriteKind.create()
# next level functionality
def next_level():
    global level, enemy_speed, max_enemies, player_speed
    level += 1
    enemy_speed += 10
    # Increase enemy speed with each level
    max_enemies += 2
    # Increase the number of enemies per level
    info.change_score_by(5)
    # Bonus points on level up
    player_speed += 10
    # Increase player speed with each level
    controller.move_sprite(player2, player_speed, player_speed)

# Spawn a power-up that boosts player's actions
def spawn_powerUp():
    powerUpType = Math.random_range(0, 2)
    # Randomly select power-up type
    powerUp: Sprite = None
    if powerUpType == 0:
            powerUp = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . f f f f f . f f f f f . .
                . . f f 2 2 2 f f f 2 2 2 f f .
                . . f 2 2 2 2 2 f 2 2 2 2 2 f .
                . . f 2 2 2 2 2 2 2 1 1 2 2 f .
                . . f 2 2 2 2 2 2 2 1 1 2 2 f .
                . . f 2 2 2 2 2 2 2 2 2 2 2 f .
                . . f f 2 2 2 2 2 2 2 2 2 f f .
                . . . f f 2 2 2 2 2 2 2 f f . .
                . . . . f f 2 2 2 2 2 f f . . .
                . . . . . f f 2 2 2 f f . . . .
                . . . . . . f f 2 f f . . . . .
                . . . . . . . f f f . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
            """),
                SpriteKind.food)
            powerUp.set_kind(SpriteKind.food)
    elif powerUpType == 1:
            powerUp = sprites.create(img("""
                ..........bbbbbbbbbbbb..........
                .......bbb331111333333bbb.......
                .....cbb3331111113333333bbb.....
                ....cb33333311113333333111db....
                ...cb3111133333333333311111db...
                .ccbb1111113333333333311111ddcc.
                ccbbd1111113333333333331111ddbcc
                cbbbdd11111333333111333311ddbbbc
                cbbbdddd1133333311111333bbbbbbbc
                .cbbbddddbbb33331111dbbbbbbbbbc.
                .ccbbbbbbbbbbbbbbdddbbbbbbbbbcc.
                ...cccbbbbbbbbbbbbbbbbbbbbccc...
                ......cccccccccccccccccccc......
                ............bbbd11bb............
                ...........bbbdd111bb...........
                ..........bbbdddd11dbb..........
            """),
                SpriteKind.Shield)
    elif powerUpType == 2:
            powerUp = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . b d b . . . . . .
                . . . . . . . b d b c . . . . .
                . . . . b b c 5 5 5 c b b . . .
                . . . . b 5 5 5 1 5 5 5 b . . .
                . . . c c 5 5 5 1 5 5 5 c c . .
                . . b b 5 5 5 1 1 1 5 5 5 b b .
                . . d d 5 1 1 1 1 1 1 1 5 d d .
                . . b b 5 5 5 1 1 1 5 5 5 b b .
                . . . c c 5 5 5 1 5 5 5 c c . .
                . . . . b 5 5 5 1 5 5 5 b . . .
                . . . . b b c 5 5 5 c b b . . .
                . . . . . . c b d b c . . . . .
                . . . . . . . b d b . . . . . .
                . . . . . . . . . . . . . . . .
            """),
                SpriteKind.RapidFire)
            powerUp.set_kind(SpriteKind.RapidFire)
    powerUp.set_position(Math.random_range(0, 160), Math.random_range(0, 120)) # Random powerUp location
# Function to spawn an enemy
def spawn_enemy():
    enemy = sprites.create(assets.image("""enemy"""), SpriteKind.enemy)
        
    # Random position for enemy spawn
    enemy.set_position(randint(0, 160), randint(0, 120))
    
    # Enemy follows player
    enemy.follow(player2, enemy_speed)
    
    # Set random velocity for enemy
    enemy.set_velocity(randint(-50, 50), randint(-50, 50))

def on_a_pressed():
    projectile: Sprite = None
    speed = 200
    
    if current_direction == 0:
            # Right
            projectile_image = img("""
                    . . . 2 . . .
                    2 2 2 2 2 . .
                    2 2 2 2 2 2 2
                    2 2 2 2 2 . .
                    . . . 2 . . .
                """)
            projectile = sprites.create_projectile_from_sprite(projectile_image, player2, 200, 0)
    elif current_direction == 1:
            # Left
            projectile_image = img("""
                . . . 2 . . .
                . . 2 2 2 2 2
                2 2 2 2 2 2 2
                . . 2 2 2 2 2
                . . . 2 . . .
            """)
            projectile = sprites.create_projectile_from_sprite(projectile_image, player2, -200, 0)
    elif current_direction == 2:
            # Up
            projectile_image = img("""
                . . 2 . .
                . . 2 . .
                . 2 2 2 .
                2 2 2 2 2
                . 2 2 2 .
                . 2 2 2 .
                . 2 2 2 .
            """)
            projectile = sprites.create_projectile_from_sprite(projectile_image, player2, 0, -200)
    elif current_direction == 3:
            # Down
            projectile_image = img("""
                . 2 2 2 .
                . 2 2 2 .
                . 2 2 2 .
                2 2 2 2 2
                . 2 2 2 .
                . . 2 . .
                . . 2 . .
            """)
            projectile = sprites.create_projectile_from_sprite(projectile_image, player2, 0, 200) 
    projectile.set_kind(SpriteKind.projectile)

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Update player direction based on movement
def on_right_pressed():
    global current_direction
    current_direction = 0

def on_left_pressed():
    global current_direction
    current_direction = 1

def on_up_pressed():
    global current_direction
    current_direction = 2

def on_down_pressed():
    global current_direction
    current_direction = 3

# calling the respective function based on direction pressed
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)


# Destroy enemy when hit by projectile
def on_projectile_enemy_overlap(projectile, enemy):
    enemy.destroy(effects.ashes, 100)
    projectile.destroy()
    # Custom tone for enemy destruction
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    info.change_score_by(1)

sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_projectile_enemy_overlap)

# Damage player when contacted by enemy
def on_player_enemy_overlap(player, enemy):
    global shield_active
    if not shield_active:
        info.change_life_by(-1)
        # Play a sound effect when the player takes damage
        music.play_tone(392, music.beat(BeatFraction.WHOLE))  
    enemy.destroy()

sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_player_enemy_overlap)

# Power-up effects: add life and also temporary speed boost
def on_overlap_food(player, powerUp):
    powerUp.destroy()
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    info.change_life_by(1)  # Increase player's life by 1
    player.vx *= 1.5  # Increase player speed
    player.vy *= 1.5
    pause(3000)  # Effect lasts 3 seconds
    player.vx /= 1.5  # Restore original speed
    player.vy /= 1.5

sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap_food)

# Power-up effects: Rapid Fire explosion
def on_overlap_rapid_fire(player, powerUp):
    powerUp.destroy()
    grenade_radius = 40

    # Explosion effect for visual feedback
    player.start_effect(effects.fire, 500)  # Brief fire effect

    # Play sound effect for explosion
    music.power_up.play_until_done()

    # Find and destroy enemies within radius
    for enemy in sprites.all_of_kind(SpriteKind.enemy):
        distance = Math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)

        if distance <= grenade_radius:
            enemy.destroy(effects.ashes, 100)
            info.change_score_by(1)

sprites.on_overlap(SpriteKind.player, SpriteKind.RapidFire, on_overlap_rapid_fire)

# Power-up effects: Shield effect
def on_overlap_shield(player, powerUp):
    global shield, shield_active

    powerUp.destroy()
    shield_active = True

    # Start shield activation sound in a loop
    def play_shield_sound():
        while shield_active:
            music.play_tone(Note.C, 500)  # tone for shield activation

    # Run the sound loop in the background
    control.run_in_parallel(play_shield_sound)
    # Create an invisible shield that follows the player
    shield = sprites.create(img("""
        . . . . . b b b b b b . . . . .
        . . . b b 9 9 9 9 9 9 b b . . .
        . . b b 9 9 9 9 9 9 9 9 b b . .
        . b b 9 d 9 9 9 9 9 9 9 9 b b .
        . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
        . b 5 3 3 3 d 9 9 9 9 d d 5 b .
        . b d 5 3 3 3 3 3 3 3 d 5 b b .
        . . b d 5 d 3 3 3 3 5 5 b b . .
        . . . b b 5 5 5 5 5 5 b b . . .
        . . . . . b b b b b b . . . . .
    """), SpriteKind.projectile)  # Use a unique kind if needed

    shield.set_position(player.x, player.y)
    shield.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)

    # Make the shield follow the player
    def update_shield_position():
        if shield_active and shield:
            shield.set_position(player.x, player.y)

    game.on_update(update_shield_position)

    # Destroy enemies that touch the shield
    def shield_enemy_overlap(shield, enemy):
        if shield_active:
            enemy.destroy(effects.ashes, 100)
            info.change_score_by(1)

    # Keep checking for overlaps with enemies as long as shield is active
    def continuously_destroy_enemies():
        while shield_active:
            sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, shield_enemy_overlap)
            pause(100)  # Slight delay to prevent overwhelming event checks

    control.run_in_parallel(continuously_destroy_enemies)

    # Deactivate shield after 10 seconds
    pause(10000)
    shield_active = False
    if shield:
        shield.destroy()

sprites.on_overlap(SpriteKind.player, SpriteKind.Shield, on_overlap_shield)


# Setup the game
def setupGame():
    global player2
    player2 = sprites.create(img("""
        . . . . . . f f f f . .
        . . . . f f f 2 2 f f f
        . . . f f f 2 2 2 2 f f
        . . f f f e e e e e e f
        . . f f e 2 2 2 2 2 2 e
        . . f e 2 f f f f f f 2
        . . f f f f e e e e f f
        . f f e f b f 4 4 f b f
        . f f e f b f 4 4 f b f
        . f e e 4 d d d d d d 4
        f d f e e d d d d d 4 e
        f b f f e e 4 4 4 4 e e
        f b f 4 f 2 2 2 2 2 2 f
        f c f . f 2 2 2 2 2 2 f
        . f f . f 4 4 5 5 4 4 f
    """),
                    SpriteKind.player)
    

    controller.move_sprite(player2, player_speed, player_speed)
    # Allows player to move freely
    player2.set_stay_in_screen(True)
    info.set_score(0) # set initial score to zero
    info.set_life(4) # set initial number of lives to 4

    # Game loop to spawn enemies periodically
    def on_update_interval():
        if len(sprites.all_of_kind(SpriteKind.enemy)) < max_enemies:
            spawn_enemy()
    game.on_update_interval(1000, on_update_interval)

    # Spawn power-ups occasionally
    def on_update_interval_ups():
        if len(sprites.all_of_kind(SpriteKind.food)) < max_food:
            spawn_powerUp()
    game.on_update_interval(10000, on_update_interval_ups)
   

player2: Sprite = None
player_speed = 0
# Track if rapid fire is active
invincible = False
# Track if shield is active
rapid_fire_active = False
shield_active = False
shield: Sprite = None
high_score = 0
current_direction = 0
score = 0
level = 1
# To store the player's shooting direction
max_enemies = 8
# Set maximum number of enemies allowed on screen
max_food = 3
# Set maximum number of Food allowed on screen
enemy_speed = 10
# Track if invincibility is active
player_speed = 100
# Variable to adjust player speed
# Set a background image
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffff
        ffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffc
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffff
        fffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffffffffffff
        fff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbffffffffffff
        ffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffff
        f33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccffffffffffffffffffff
        ff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffff
        ffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffff
        fffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffff
        fffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcfffff
        ffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffff
        fffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcffffffffffff
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffff
        ffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffff
        ffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffff
        fffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccf
        ccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        bbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbb
        bbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbb
        bbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbb
        bbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbb
        bbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbb
        3bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb33333333
        333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb
        cc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccc
        cccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcc
        cccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccc
        cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccc
        bbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbb
        bbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bb
        dddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddd
        dddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33d
        dddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbd
        ddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbdd
        ddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33ddddddddddddd
        ddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbdddddddddddddd
        ddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3ddddddddddddddd
        d333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333dddddddddddddddddd
        333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3
        33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333d
        33ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd33
        d333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333dddddddddddddddd
        ddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3d
        b3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbb
        bb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbb
        bbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbb
        b3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbb
        dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddd
        dddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddd
        dddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddd
        dd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddd
        3333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd333
        33333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
"""))

# Start the game
setupGame()
# Apply new speed

def on_on_update():
    if info.score() >= 20 * level:
        # Higher threshold per level
        next_level()
game.on_update(on_on_update)
