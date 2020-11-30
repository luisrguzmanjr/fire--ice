@namespace
class SpriteKind:
    heroProjectile = SpriteKind.create()
    enemyProjectile = SpriteKind.create()
    specialEProjectile = SpriteKind.create()
    specialHProjectile = SpriteKind.create()
    Bonus = SpriteKind.create()
    Health = SpriteKind.create()
    ArmorBar = SpriteKind.create()
    heroIceProjectile = SpriteKind.create()
    Helper = SpriteKind.create()
    Bkgrd = SpriteKind.create()

def on_on_created(sprite):
    global vyEnemy
    vyEnemy = 50
    sprite.set_position(140, randint(0, 115))
    sprite.set_velocity(0, vyEnemy)
    sprite.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
sprites.on_created(SpriteKind.enemy, on_on_created)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    hitPlayer()
sprites.on_overlap(SpriteKind.enemyProjectile, SpriteKind.player, on_on_overlap)

def on_b_pressed():
    shootAtEnemy()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def createHealthShip():
    global shipSprite, bCreateHealthShip
    shipSprite = sprites.create(img("""
            . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c b . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . c 2 . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . e 2 . . . . . . . 
                    . . . . . . e e 4 e . . . . . . 
                    . . . . . . e 2 4 e . . . . . . 
                    . . . . . c c c e e e . . . . . 
                    . . . . e e 2 2 2 4 e e . . . . 
                    . . c f f f c c e e f f e e . . 
                    . c c c c e e 2 2 2 2 4 2 e e . 
                    c c c c c c e e 2 2 2 4 2 2 e e 
                    c c c c c c e e 2 2 2 2 4 2 e e
        """),
        SpriteKind.Helper)
    shipSprite.set_position(160, 10)
    shipSprite.set_velocity(-26, 0)
    shipSprite.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
    animation.run_image_animation(shipSprite, shipFrames, 50, True)
    bCreateHealthShip = 1
def shootAtEnemy():
    global snowPower, icePower, freezePower, snowPower2, snowPower3
    animation.run_image_animation(mySprite, playerframes, 50, False)
    snowPower = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 1 . . . . . 1 . . . . . . 
                    . . 1 1 1 . . . 1 1 1 . . . . . 
                    . . . 1 . . 1 . . 1 . . . . . . 
                    . . . . . 1 1 1 . . . . . . . . 
                    . . . 1 . . 1 . . 1 . . . . . . 
                    . . 1 1 1 . . . 1 1 1 . . . . . 
                    . . . 1 . . . . . 1 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        75,
        0)
    music.pew_pew.play()
    snowPower.set_kind(SpriteKind.projectile)
    if bIcePower:
        icePower = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 9 . . . . . . . . . . 
                            . . . . 9 9 9 . . . . . . . . . 
                            . . . . . 9 . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 9 . . . . . . . . 
                            . . . . . . 9 9 9 . . . . . . . 
                            . . . . . . . 9 . . . . . . . . 
                            . . . . . . 9 9 9 . . . . . . . 
                            . . . . . . . 9 . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 9 . . . . . . . . . . 
                            . . . . 9 9 9 . . . . . . . . . 
                            . . . . . 9 . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            90,
            0)
        icePower.set_kind(SpriteKind.heroIceProjectile)
    if bHSpecialPower:
        freezePower = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 6 6 6 6 . . . . . . 
                            . . . . 6 6 6 5 5 6 6 6 . . . . 
                            . . . 7 7 7 7 6 6 6 6 6 6 . . . 
                            . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
                            . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
                            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
                            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
                            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
                            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
                            . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
                            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
                            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
                            . . . . 6 6 8 8 8 8 6 6 . . . . 
                            . . . . . . 6 6 6 6 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            80,
            0)
        freezePower.set_kind(SpriteKind.specialHProjectile)
    if bDoubleHPower:
        snowPower2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 1 . . . . . 1 . . . . . . 
                            . . 1 1 1 . . . 1 1 1 . . . . . 
                            . . . 1 . . 1 . . 1 . . . . . . 
                            . . . . . 1 1 1 . . . . . . . . 
                            . . . 1 . . 1 . . 1 . . . . . . 
                            . . 1 1 1 . . . 1 1 1 . . . . . 
                            . . . 1 . . . . . 1 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            75,
            20)
        snowPower2.set_kind(SpriteKind.projectile)
    if bTripleHPower:
        snowPower3 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 1 . . . . . 1 . . . . . . 
                            . . 1 1 1 . . . 1 1 1 . . . . . 
                            . . . 1 . . 1 . . 1 . . . . . . 
                            . . . . . 1 1 1 . . . . . . . . 
                            . . . 1 . . 1 . . 1 . . . . . . 
                            . . 1 1 1 . . . 1 1 1 . . . . . 
                            . . . 1 . . . . . 1 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            75,
            -20)
        snowPower3.set_kind(SpriteKind.projectile)
def hitPlayer():
    global ctrDamage, maxHealth, currHealth, bTripleHPower, bTripleBonus, bDoubleHPower, bDoubleBonus, bIcePower, bIceBonus
    if hitDamage == -0.5 and ctrDamage < maxArmor:
        ctrDamage += 1
        hitArmor()
        music.play_tone(294, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(387, music.beat(BeatFraction.SIXTEENTH))
        music.play_tone(584, music.beat(BeatFraction.SIXTEENTH))
    else:
        if hitDamage == -0.5:
            hitArmor()
            maxHealth = maxArmor + 1
            currHealth = maxHealth
            fillHealthBar(myHealthBar, maxHealth, currHealth)
        info.change_life_by(-1)
        music.power_down.play()
        ctrDamage = 0
        # skip
        if bTripleHPower:
            bTripleHPower = 0
            bTripleBonus = 0
        elif bDoubleHPower:
            bDoubleHPower = 0
            bDoubleBonus = 0
        elif bIcePower:
            bIcePower = 0
            bIceBonus = 0
    if info.life() == 0:
        game.over(False, effects.slash)
def sendBonus():
    global bCreateHealthShip, bNeedHealth, bNeedBonus, armorBonus, snowPower3, snowPower2, icePower
    if Math.percent_chance(0.2) and maxArmor < 2 or Math.percent_chance(0.2) and bTripleBonus == 0:
        createBonusShip()
        bCreateHealthShip = 0
        bNeedHealth = 0
        bNeedBonus = 1
    if bCreateBonusShip:
        if bTripleBonus:
            armorBonus = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . e e e e e e . . . . . 
                                    . . . . e 5 4 4 4 4 4 e . . . . 
                                    . . . . e 4 5 5 4 4 4 e . . . . 
                                    . . . . e 4 4 4 5 5 4 e . . . . 
                                    . . . . e 4 4 4 4 4 5 e . . . . 
                                    . . . . . e 4 4 4 4 e . . . . . 
                                    . . . . . . e 4 4 e . . . . . . 
                                    . . . . . . . e e . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                shipSprite,
                0,
                10)
            armorBonus.set_kind(SpriteKind.Bonus)
        elif bDoubleBonus:
            snowPower3 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . 5 5 5 . . . . . 
                                    . . . . . . . . . . 5 . . . . . 
                                    . . . . . . . . 5 5 5 . . . . . 
                                    . . . . . . . . . . 5 . . . . . 
                                    . . . . 5 . 5 . 5 5 5 . . . . . 
                                    . . . . . 5 . . . . . . . . . . 
                                    . . . . 5 . 5 . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                shipSprite,
                0,
                10)
            snowPower3.set_kind(SpriteKind.Bonus)
        elif bIceBonus:
            snowPower2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . 5 5 5 . . . . . 
                                    . . . . . . . . . . 5 . . . . . 
                                    . . . . . . . . 5 5 5 . . . . . 
                                    . . . . . . . . 5 . . . . . . . 
                                    . . . . 5 . 5 . 5 5 5 . . . . . 
                                    . . . . . 5 . . . . . . . . . . 
                                    . . . . 5 . 5 . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                shipSprite,
                0,
                10)
            snowPower2.set_kind(SpriteKind.Bonus)
        else:
            icePower = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . 9 . . . . . . . . . . 
                                    . . . . 9 9 9 . . . . . . . . . 
                                    . . . . . 9 . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . 9 . . . . . . . . 
                                    . . . . . . 9 9 9 . . . . . . . 
                                    . . . . . . . 9 . . . . . . . . 
                                    . . . . . . 9 9 9 . . . . . . . 
                                    . . . . . . . 9 . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . 9 . . . . . . . . . . 
                                    . . . . 9 9 9 . . . . . . . . . 
                                    . . . . . 9 . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                shipSprite,
                0,
                10)
            icePower.set_kind(SpriteKind.Bonus)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.specialEProjectile,
    on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    sprite.destroy()
    getHealth()
sprites.on_overlap(SpriteKind.Health, SpriteKind.player, on_on_overlap3)

def hitArmor():
    global currHealth
    if currHealth > targetHealth:
        currHealth += -1
        fillHealthBar(myHealthBar, maxHealth, currHealth)

def on_on_overlap4(sprite, otherSprite):
    sprite.destroy()
    getBonus()
sprites.on_overlap(SpriteKind.Bonus, SpriteKind.player, on_on_overlap4)

# BEGIN health bar
def fillHealthBar(healthBar: Sprite, maxHealth: number, currHealth: number):
    global percent, healthBarImage
    percent = Math.constrain(currHealth / maxHealth, 0, 1)
    healthBarImage = healthBar.image
    healthBarImage.draw_rect(1, 1, healthBar.width - 2, 2, 2)
    healthBarImage.draw_rect(1, 1, (healthBar.width - 2) * percent, 2, 7)
    healthBarImage.draw_rect(0, 0, healthBar.width, healthBar.height, 12)
def createCloud():
    global cloud
    cloud = sprites.create_projectile_from_side(clouds[randint(0, len(clouds) - 1)], -30, 0)
    cloud.bottom = randint(30, 55)
    cloud.z = -2
    cloud.set_kind(SpriteKind.Bkgrd)

def on_b_repeated():
    shootAtEnemy()
controller.B.on_event(ControllerButtonEvent.REPEATED, on_b_repeated)

def on_on_overlap5(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy()
sprites.on_overlap(SpriteKind.heroIceProjectile,
    SpriteKind.enemyProjectile,
    on_on_overlap5)

def on_on_overlap6(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.Health,
    SpriteKind.enemyProjectile,
    on_on_overlap6)

def on_on_overlap7(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.enemyProjectile,
    on_on_overlap7)

def on_on_overlap8(sprite, otherSprite):
    global bFrozen, vyPrevEnemy, vyEnemy, bHSpecialPower, maxFrozen
    sprite.destroy()
    if bFrozen == 0:
        animation.stop_animation(animation.AnimationTypes.ALL, enemySprite)
        bFrozen = 1
        if vyEnemy > 0:
            vyPrevEnemy = vyEnemy
        vyEnemy = 0
        otherSprite.set_velocity(0, vyEnemy)
        otherSprite.start_effect(effects.blizzard, 2000)
        bHSpecialPower = 0
        maxFrozen = 0
sprites.on_overlap(SpriteKind.specialHProjectile,
    SpriteKind.enemy,
    on_on_overlap8)

def getBonus():
    global bCreateBonusShip, bNeedBonus, hitDamage, ctrDamage, maxArmor, maxHealth, currHealth, shieldSprite, bTripleBonus, bTripleHPower, bDoubleBonus, bDoubleHPower, bIceBonus, bIcePower
    bCreateBonusShip = 0
    if bNeedBonus:
        bNeedBonus = 0
        if bTripleBonus:
            hitDamage = -0.5
            ctrDamage = 0
            maxArmor += 1
            maxHealth = maxArmor + 1
            currHealth = maxHealth
            if maxArmor == 1:
                shieldSprite = sprites.create(img("""
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . e e e e e e . . . . . 
                                            . . . . e 5 4 4 4 4 4 e . . . . 
                                            . . . . e 4 5 5 4 4 4 e . . . . 
                                            . . . . e 4 4 4 5 5 4 e . . . . 
                                            . . . . e 4 4 4 4 4 5 e . . . . 
                                            . . . . . e 4 4 4 4 e . . . . . 
                                            . . . . . . e 4 4 e . . . . . . 
                                            . . . . . . . e e . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    SpriteKind.ArmorBar)
                shieldSprite.set_position(48, 115)
                shieldSprite.z = 1
                shieldSprite = sprites.create(img("""
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . e e e e e e . . . . . 
                                            . . . . e 5 4 4 4 4 4 e . . . . 
                                            . . . . e 4 5 5 4 4 4 e . . . . 
                                            . . . . e 4 4 4 5 5 4 e . . . . 
                                            . . . . e 4 4 4 4 4 5 e . . . . 
                                            . . . . . e 4 4 4 4 e . . . . . 
                                            . . . . . . e 4 4 e . . . . . . 
                                            . . . . . . . e e . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    SpriteKind.ArmorBar)
                shieldSprite.set_position(48 + maxArmor * 3, 115)
                shieldSprite.z = 1
            else:
                shieldSprite = sprites.create(img("""
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . e e e e e e . . . . . 
                                            . . . . e 5 4 4 4 4 4 e . . . . 
                                            . . . . e 4 5 5 4 4 4 e . . . . 
                                            . . . . e 4 4 4 5 5 4 e . . . . 
                                            . . . . e 4 4 4 4 4 5 e . . . . 
                                            . . . . . e 4 4 4 4 e . . . . . 
                                            . . . . . . e 4 4 e . . . . . . 
                                            . . . . . . . e e . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    """),
                    SpriteKind.ArmorBar)
                shieldSprite.set_position(48 + maxArmor * 3, 115)
                shieldSprite.z = 1
            myHealthBar.set_position(25, 117)
            fillHealthBar(myHealthBar, maxHealth, currHealth)
            game.set_dialog_cursor(img("""
                ........................
                                .....ffff...............
                                ...fff22fff.............
                                ..fff2222fff............
                                .fffeeeeeefff...........
                                .ffe222222eef...........
                                .fe2ffffff2ef...........
                                .ffffeeeeffff...........
                                ffefbf44fbfeff..........
                                fee41fddf14eef..........
                                .ffffdddddeef...........
                                fddddf444eef............
                                fbbbbf2222f4e...........
                                fbbbbf2222fd4...........
                                .fccf45544f44...........
                                ..ffffffff..............
                                ....ff..ff..............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
            """))
            game.show_long_text("You got " + str((maxArmor + 1)) + " hit armor!",
                DialogLayout.BOTTOM)
        elif bDoubleBonus:
            bTripleBonus = 1
            bTripleHPower = 1
            game.set_dialog_cursor(img("""
                ........................
                                .....ffff...............
                                ...fff22fff.............
                                ..fff2222fff............
                                .fffeeeeeefff...........
                                .ffe222222eef...........
                                .fe2ffffff2ef...........
                                .ffffeeeeffff...........
                                ffefbf44fbfeff..........
                                fee41fddf14eef..........
                                .ffffdddddeef...........
                                fddddf444eef............
                                fbbbbf2222f4e...........
                                fbbbbf2222fd4...........
                                .fccf45544f44...........
                                ..ffffffff..............
                                ....ff..ff..............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
            """))
            game.show_long_text("You got triple power!  Try not to get hit or you will lose it!",
                DialogLayout.BOTTOM)
        elif bIceBonus:
            bDoubleBonus = 1
            bDoubleHPower = 1
            game.set_dialog_cursor(img("""
                ........................
                                .....ffff...............
                                ...fff22fff.............
                                ..fff2222fff............
                                .fffeeeeeefff...........
                                .ffe222222eef...........
                                .fe2ffffff2ef...........
                                .ffffeeeeffff...........
                                ffefbf44fbfeff..........
                                fee41fddf14eef..........
                                .ffffdddddeef...........
                                fddddf444eef............
                                fbbbbf2222f4e...........
                                fbbbbf2222fd4...........
                                .fccf45544f44...........
                                ..ffffffff..............
                                ....ff..ff..............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
            """))
            game.show_long_text("You got double power! Try not to get hit or you will lose it!",
                DialogLayout.BOTTOM)
        else:
            bIceBonus = 1
            bIcePower = 1
            game.set_dialog_cursor(img("""
                ........................
                                .....ffff...............
                                ...fff22fff.............
                                ..fff2222fff............
                                .fffeeeeeefff...........
                                .ffe222222eef...........
                                .fe2ffffff2ef...........
                                .ffffeeeeffff...........
                                ffefbf44fbfeff..........
                                fee41fddf14eef..........
                                .ffffdddddeef...........
                                fddddf444eef............
                                fbbbbf2222f4e...........
                                fbbbbf2222fd4...........
                                .fccf45544f44...........
                                ..ffffffff..............
                                ....ff..ff..............
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
                                ........................
            """))
            game.show_long_text("You got ice power! Try not to get hit or you will lose it!",
                DialogLayout.BOTTOM)
        music.play_melody("E E G - G G B C5 ", 480)
def getHealth():
    global bCreateHealthShip, bNeedHealth
    bCreateHealthShip = 0
    if bNeedHealth:
        bNeedHealth = 0
        info.change_life_by(1)
        music.power_up.play()
def sendHealth():
    global bCreateBonusShip, bNeedBonus, bNeedHealth, healthBonus
    if Math.percent_chance(0.1):
        createHealthShip()
        bCreateBonusShip = 0
        bNeedBonus = 0
        bNeedHealth = 1
    if bCreateHealthShip:
        healthBonus = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 2 . . 2 . . . . . . 
                            . . . . . 2 2 2 2 2 2 . . . . . 
                            . . . . 2 2 2 2 2 2 2 2 . . . . 
                            . . . . 2 2 2 2 2 2 2 2 . . . . 
                            . . . . 2 2 2 2 2 2 2 2 . . . . 
                            . . . . . 2 2 2 2 2 2 . . . . . 
                            . . . . . . 2 2 2 2 . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            shipSprite,
            0,
            10)
        healthBonus.set_kind(SpriteKind.Health)

def on_on_overlap9(sprite, otherSprite):
    global vyEnemy, msTimer, bHSpecialPower, bDoublePower, bTriplePower, bESpecialPower
    sprite.destroy()
    music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(587, music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(784, music.beat(BeatFraction.SIXTEENTH))
    info.change_score_by(1)
    if info.score() % 20 == 0:
        if bFrozen:
            vyEnemy += 0
        else:
            if vyEnemy >= 15 and vyEnemy <= 80:
                vyEnemy += randint(-10, 10)
            else:
                vyEnemy = randint(15, 80)
        if msTimer > minTimer:
            msTimer += -100
        bHSpecialPower = 1
    if info.score() == 80:
        game.set_dialog_cursor(img("""
            . . . . . c c c c c c c . . . . 
                        . . . . c 6 7 7 7 7 7 6 c . . . 
                        . . . c 7 c 6 6 6 6 c 7 6 c . . 
                        . . c 6 7 6 f 6 6 f 6 7 7 c . . 
                        . . c 7 7 7 7 7 7 7 7 7 7 c . . 
                        . . f 7 8 1 f f 1 6 7 7 7 f . . 
                        . . f 6 f 1 f f 1 f 7 7 7 f . . 
                        . . . f f 2 2 2 2 f 7 7 6 f . . 
                        . . c c f 2 2 2 2 7 7 6 f c . . 
                        . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
                        c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
                        f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
                        f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
                        f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
                        . f 6 1 1 1 1 1 6 6 6 6 c . . . 
                        . . f f c c c c c c c c . . . .
        """))
        game.show_long_text("Prepare for double fire!", DialogLayout.BOTTOM)
        bDoublePower = 1
    if info.score() == 100:
        game.set_dialog_cursor(img("""
            . . . . . c c c c c c c . . . . 
                        . . . . c 6 7 7 7 7 7 6 c . . . 
                        . . . c 7 c 6 6 6 6 c 7 6 c . . 
                        . . c 6 7 6 f 6 6 f 6 7 7 c . . 
                        . . c 7 7 7 7 7 7 7 7 7 7 c . . 
                        . . f 7 8 1 f f 1 6 7 7 7 f . . 
                        . . f 6 f 1 f f 1 f 7 7 7 f . . 
                        . . . f f 2 2 2 2 f 7 7 6 f . . 
                        . . c c f 2 2 2 2 7 7 6 f c . . 
                        . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
                        c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
                        f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
                        f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
                        f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
                        . f 6 1 1 1 1 1 6 6 6 6 c . . . 
                        . . f f c c c c c c c c . . . .
        """))
        game.show_long_text("Triple fire will melt you!", DialogLayout.BOTTOM)
        bTriplePower = 1
        effects.blizzard.start_screen_effect()
    if info.score() == 150:
        game.set_dialog_cursor(img("""
            . . . . . c c c c c c c . . . . 
                        . . . . c 6 7 7 7 7 7 6 c . . . 
                        . . . c 7 c 6 6 6 6 c 7 6 c . . 
                        . . c 6 7 6 f 6 6 f 6 7 7 c . . 
                        . . c 7 7 7 7 7 7 7 7 7 7 c . . 
                        . . f 7 8 1 f f 1 6 7 7 7 f . . 
                        . . f 6 f 1 f f 1 f 7 7 7 f . . 
                        . . . f f 2 2 2 2 f 7 7 6 f . . 
                        . . c c f 2 2 2 2 7 7 6 f c . . 
                        . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
                        c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
                        f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
                        f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
                        f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
                        . f 6 1 1 1 1 1 6 6 6 6 c . . . 
                        . . f f c c c c c c c c . . . .
        """))
        game.show_long_text("Now it is time you feel my full wrath!",
            DialogLayout.BOTTOM)
        effects.blizzard.end_screen_effect()
        bESpecialPower = 1
sprites.on_overlap(SpriteKind.heroProjectile, SpriteKind.player, on_on_overlap9)

def on_on_overlap10(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.Bonus,
    SpriteKind.enemyProjectile,
    on_on_overlap10)

def setFrame():
    global playerframes, enemyFrames, shipFrames, clouds, trees, grassImages
    playerframes = [sprites.castle.hero_side_attack_right4,
        sprites.castle.hero_side_attack_right3,
        sprites.castle.hero_side_attack_right2,
        sprites.castle.hero_side_attack_right1,
        sprites.castle.hero_side_attack_right4]
    animation.run_image_animation(mySprite, playerframes, 50, False)
    enemyFrames = [sprites.builtin.forest_snake0,
        sprites.builtin.forest_snake1,
        sprites.builtin.forest_snake2,
        sprites.builtin.forest_snake3,
        sprites.builtin.forest_snake4,
        sprites.builtin.forest_snake5,
        sprites.builtin.forest_snake6,
        sprites.builtin.forest_snake7]
    animation.run_image_animation(enemySprite, enemyFrames, 50, True)
    shipFrames = [sprites.space.space_red_ship,
        sprites.space.space_orange_ship,
        sprites.space.space_pink_ship,
        sprites.space.space_blue_ship,
        sprites.space.space_green_ship]
    clouds = [img("""
            ............................bb.....................
                    .........................bbbbbbb...................
                    ........................bbbbbbbbbbbb...............
                    .......................bbbbbbbbbbbbbb..............
                    ......................bbbbbbbbbbbbbbbb.............
                    .....................bbbbbbbbbbbbbbbbb.............
                    ..................bbbbbbbbbbbbbbbbbbbbb............
                    ...............bbbbbbbbbbbbbbbbbbbbbbbbb...........
                    ..........bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..........
                    .........bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.........
                    ........bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.......
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.....
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    ......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    .....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb......
        """),
        img("""
            .........................bbbbb................
                    ........................bbbbbbb...............
                    ......................bbbbbbbbbb..............
                    ..................bbbbbbbbbbbbbbb.............
                    ...............bbbbbbbbbbbbbbbbbb.............
                    ..............bbbbbbbbbbbbbbbbbbbbbbbbb.......
                    .............bbbbbbbbbbbbbbbbbbbbbbbbbbb......
                    .............bbbbbbbbbbbbbbbbbbbbbbbbbbb......
                    .............bbbbbbbbbbbbbbbbbbbbbbbbbbbb.....
                    ............bbbbbbbbbbbbbbbbbbbbbbbbbbbbb.....
                    ............bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
                    ............bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb....
                    ...........bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
                    ......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    .....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    bbbbbbbbbbbbbbbbb..................bbbbbbbbb..
        """),
        img("""
            ........bbbbbbbb.................
                    .......bbbbbbbbbb................
                    ....bbbbbbbbbbbbbb...............
                    ...bbbbbbbbbbbbbbbb..............
                    ..bbbbbbbbbbbbbbbbbbbbbbb........
                    ..bbbbbbbbbbbbbbbbbbbbbbbb.......
                    .bbbbbbbbbbbbbbbbbbbbbbbbbb......
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbb.....
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbb.....
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    .....bbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ......bbbbbbbbbbbbbbbbbbbbbbbb...
                    .................................
        """),
        img("""
            ...................bbbb................................................
                    ..................bbbbbb...............................................
                    .................bbbbbbbbbbbbbb........................................
                    ................bbbbbbbbbbbbbbbb.......................................
                    ..............bbbbbbbbbbbbbbbbbbb......................................
                    ............bbbbbbbbbbbbbbbbbbbbbb.....................................
                    ...........bbbbbbbbbbbbbbbbbbbbbbb.....................................
                    ..........bbbbbbbbbbbbbbbbbbbbbbbb.....................................
                    ..........bbbbbbbbbbbbbbbbbbbbbbbbb......bbbbb.........................
                    .........bbbbbbbbbbbbbbbbbbbbbbbbbb...bbbbbbbbb........................
                    .........bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.......................
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb......................
                    ......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...................
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.................
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb................
                    ...bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...............
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..............
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..............
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.............
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb............
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..........
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb........
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ...............bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..........bbbbbbbb.......
        """),
        img("""
            ........................bbbb...........
                    .................bbbb..bbbbbb..........
                    ...............bbbbbbbbbbbbbbb.........
                    .............bbbbbbbbbbbbbbbbbb........
                    ............bbbbbbbbbbbbbbbbbbbb.......
                    .........bbbbbbbbbbbbbbbbbbbbbbbb......
                    ........bbbbbbbbbbbbbbbbbbbbbbbbb......
                    .......bbbbbbbbbbbbbbbbbbbbbbbbbbbb....
                    ......bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb...
                    .....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    .....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ....bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    ..bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                    .bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.
                    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb..
                    bbbbbbbbbbbbbbbbbb.....................
        """)]
    trees = [img("""
            ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ...................b................
                    ...................b................
                    ...................b................
                    ..................bbb...............
                    ..................bb................
                    .................bbbb...............
                    ................bbbbbb..............
                    ..................bb................
                    .................bbbb...............
                    ................bbbbbb..............
                    ...............bbbbbbbb.............
                    ..............bb..bbbbbb............
                    .................bbbb..bbb..........
                    ..................bb................
                    .................bbbb...............
                    ................bbbbbb..............
                    ...............bbbbb.bb.............
                    ..............bbbbbbbbbb............
                    ............bbbb.bbbbbbb............
                    ..........bbbbb..bbbbb.bbbb.........
                    ................bbbbbb...bbb........
                    ...............bbbbbbbb.............
                    ..............bbbbbb.bb.............
                    ...........bbbbbbbbbbbbb............
                    .........bbbbbb..bbbb.bbb...........
                    ..........bbbbb..bbbb...............
                    ................bbbbbbb.............
                    ...............bbbbbbbbb............
                    .............bbbbbbbbb..............
                    ...........bbbbbbbbbbbbbbbbb........
                    ..........bbbbbbbbbbbbbbbbb.........
                    .........bbbb.bbbbbbbb..............
                    ........bb....bbbbbbbbb.............
                    ............bbbbbbbbbbbbb...........
                    ........bbbbbbbbbbbbbbbbbbbb........
                    .......bbbbbbbbbbbbbbbbbbbbbbb......
                    ......bbbbbbbb...bbbbbbbbb..........
                    ..................bbb...............
                    ..................bbb...............
                    ..................bbb...............
        """),
        img("""
            ...................b................
                    ...................b................
                    ...................b................
                    ..................bbb...............
                    .................bbbbbb.............
                    ..................bb................
                    ...................bbbb.............
                    .................bbbbbbb............
                    ...............bbb.b................
                    ..................bbb...............
                    ...............bbbbbbb..............
                    ................bbbbbbbb............
                    ..................bb.bbbb...........
                    ..................bbb...............
                    .................bbbbbb.............
                    .............bbbbbbb.bbbb...........
                    ............bbbbb.bbb...............
                    ..................bbb...............
                    .................bbbbb..............
                    ..............bbbbbbbb..............
                    .............bbbbbbbbbb.............
                    ............bbb..bbbbbbbb...........
                    ...........bbbb.bbbbbbbb.b..........
                    ............b...bbbbbbbbb...........
                    ...............bbbbbbbbbbb..........
                    ..............bbbbbbb.bbbb..........
                    .............bbbbbbbbbbbbbbb........
                    ...........bbbb.bbbbbbb.............
                    ...............bbbbbb.bb............
                    .............bbbbbbbbbbbb...........
                    ............bbbbbbbbbbbbbb..........
                    ............bbbbbbbbbb..bbb.........
                    .........bbbbbbbbbbbbbb..bbbb.......
                    ........bb...bbbbbbbbb..............
                    ..............bbbbbbbbbbb...........
                    ............bbbb.bbbbbbbb...........
                    ........bbbb.b...bbbbbbb............
                    ................bbbbb..bbbb.........
                    .............bbbbb.bbbbbbbb.........
                    .........bbbbbb..bbbb..bbbbb........
                    ........bb.b....bbbbb.....bbb.......
                    ................bbbbb...............
                    ..................bbb...............
                    ..................bbb...............
                    ..................bbb...............
                    ..................bbb...............
                    ..................bbb...............
                    ..................bbb...............
        """),
        img("""
            ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ....................................
                    ...................b................
                    ...................b................
                    ...................b................
                    ...................b................
                    ..................bb................
                    ..................bbb...............
                    .................bbbb...............
                    ...............bbbbb................
                    ..................bb................
                    .................bbbb...............
                    .................bbbb...............
                    .................bbbbb..............
                    ................bbbbbbb.............
                    ..............bbbbbbbbbb............
                    ............bbbb..bbbbbbb...........
                    .................bbbb...............
                    .................bbbb...............
                    ................bbbbbb..............
                    ................bbbbbb..............
                    ...............bbbbbbbb.............
                    ............bbbbbbbbbbbbb...........
                    ........bbbbbbbbbbbbbbbbbbbb........
                    ...........bbbbbbbbbbbbbbbb.........
                    ................bbbbbbb.b...........
                    ..............bbbbbbbbbbbbbbbb......
                    ...........bbbbbbbbbbbbbbbbbb.......
                    ........bbbbbbbbbbbbbbbbbbb.........
                    ..........bbbbb...bbbb..............
                    ..................bbb...............
                    ..................b.b...............
                    ..................b.b...............
                    ..................bbb...............
                    ..................bbb...............
        """)]
    grassImages = [img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . b . . . 
                    . . . . b . . . 
                    . . . b b . . . 
                    . . . b b . . .
        """),
        img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . b . . . . 
                    . . . b . . . . 
                    . . . b b . b . 
                    . . . b b . b .
        """),
        img("""
            . . . . . . . . 
                    . . . . . . . . 
                    b . . . . . . . 
                    b . . b . . . . 
                    b . . b b . . . 
                    b . b b b . . . 
                    b . b b b . b . 
                    b b b b b . b .
        """),
        img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . b 
                    . . . b . . . b 
                    . . . b . . . b 
                    . . . b b . b b 
                    . . . b b . b b
        """),
        img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . b . . . . 
                    . . . b . . . . 
                    . . b b . . . . 
                    . . b b b . . . 
                    . . b b b . . . 
                    . . b b b . . .
        """),
        img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . b . . . . . . 
                    . b . . . . . . 
                    . b b . . . b . 
                    . b b . . . b . 
                    . b b . . . b .
        """)]
def createBonusShip():
    global shipSprite, bCreateBonusShip
    shipSprite = sprites.create(img("""
            . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c b . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . c 2 . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . e 2 . . . . . . . 
                    . . . . . . e e 4 e . . . . . . 
                    . . . . . . e 2 4 e . . . . . . 
                    . . . . . c c c e e e . . . . . 
                    . . . . e e 2 2 2 4 e e . . . . 
                    . . c f f f c c e e f f e e . . 
                    . c c c c e e 2 2 2 2 4 2 e e . 
                    c c c c c c e e 2 2 2 4 2 2 e e 
                    c c c c c c e e 2 2 2 2 4 2 e e
        """),
        SpriteKind.Helper)
    shipSprite.set_position(160, 10)
    shipSprite.set_velocity(-26, 0)
    shipSprite.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
    animation.run_image_animation(shipSprite, shipFrames, 50, True)
    bCreateBonusShip = 1

def on_on_overlap11(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.specialEProjectile,
    SpriteKind.heroProjectile,
    on_on_overlap11)

def on_on_overlap12(sprite, otherSprite):
    sprite.destroy()
    hitPlayer()
sprites.on_overlap(SpriteKind.specialEProjectile,
    SpriteKind.player,
    on_on_overlap12)

def on_on_overlap13(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.Bonus, SpriteKind.enemy, on_on_overlap13)

def on_on_overlap14(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.heroIceProjectile,
    SpriteKind.enemy,
    on_on_overlap14)

def on_on_created2(sprite):
    sprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
sprites.on_created(SpriteKind.player, on_on_created2)

def on_on_overlap15(sprite, otherSprite):
    sprite.destroy()
    firePower.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . 1 1 1 1 1 1 1 . . . . . . 
                . . 1 c a a a a a 9 1 . . . . . 
                . . 1 c c a a a 9 9 1 . . . . . 
                . . 1 c a a 1 a a 9 1 . . . . . 
                . . 1 a a 1 1 1 a a 1 . . . . . 
                . . 1 c a a 1 a a 9 1 . . . . . 
                . . 1 c c a a a 9 9 1 . . . . . 
                . . 1 c a a a a a 9 1 . . . . . 
                . . . 1 1 1 1 1 1 1 . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    firePower.set_kind(SpriteKind.heroProjectile)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap15)

def createTree():
    global tree
    tree = sprites.create_projectile_from_side(trees[randint(0, len(trees) - 1)], -50, 0)
    tree.bottom = 100
    tree.z = -1
    tree.set_kind(SpriteKind.Bkgrd)
grass: Sprite = None
fireballPower: Sprite = None
firePower3: Sprite = None
firePower2: Sprite = None
tree: Sprite = None
firePower: Sprite = None
grassImages: List[Image] = []
trees: List[Image] = []
enemyFrames: List[Image] = []
bESpecialPower = 0
bTriplePower = 0
bDoublePower = 0
healthBonus: Sprite = None
shieldSprite: Sprite = None
maxFrozen = 0
vyPrevEnemy = 0
bFrozen = 0
clouds: List[Image] = []
cloud: Sprite = None
healthBarImage: Image = None
percent = 0
armorBonus: Sprite = None
bCreateBonusShip = 0
bNeedBonus = 0
bNeedHealth = 0
bIceBonus = 0
bDoubleBonus = 0
bTripleBonus = 0
maxArmor = 0
ctrDamage = 0
snowPower3: Sprite = None
bTripleHPower = 0
snowPower2: Sprite = None
bDoubleHPower = 0
freezePower: Sprite = None
bHSpecialPower = 0
icePower: Sprite = None
bIcePower = 0
snowPower: Sprite = None
playerframes: List[Image] = []
bCreateHealthShip = 0
shipFrames: List[Image] = []
shipSprite: Sprite = None
vyEnemy = 0
targetHealth = 0
currHealth = 0
maxHealth = 0
myHealthBar: Sprite = None
enemySprite: Sprite = None
mySprite: Sprite = None
hitDamage = 0
msTimer = 0
minTimer = 0
game.splash("Fire & Ice")
minTimer = 100
msTimer = 1000
hitDamage = -1
info.set_life(3)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15555555dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1555555555dfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15555555d555bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15dd55555555bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15d55555555dbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff155555dd555dbffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff155555d5d555bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff155555555555bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15555dd55555bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1555dd5555dfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff15555555dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
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
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
mySprite = sprites.create(img("""
        ....ffffff..............
            ..ffeeeef2f.............
            .ffeeeef222f............
            .feeeffeeeef............
            .ffffee2222ef...........
            .fe222ffffe2f...........
            fffffffeeefff...........
            ffe44ebf44eef...........
            fee4d41fddef............
            .feee4ddddf.............
            ..fdde444ef.............
            ..fdde22ccc.............
            ...eef22cdc.............
            ...f4444cddc............
            ....fffffcddc...........
            .....fff..cddc..........
            ...........cdc..........
            ............cc..........
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
enemySprite = sprites.create(img("""
        . . . . . c c c c c c c . . . . 
            . . . . c 6 7 7 7 7 7 6 c . . . 
            . . . c 7 c 6 6 6 6 c 7 6 c . . 
            . . c 6 7 6 f 6 6 f 6 7 7 c . . 
            . . c 7 7 7 7 7 7 7 7 7 7 c . . 
            . . f 7 8 1 f f 1 6 7 7 7 f . . 
            . . f 6 f 1 f f 1 f 7 7 7 f . . 
            . . . f f 2 2 2 2 f 7 7 6 f . . 
            . . c c f 2 2 2 2 7 7 6 f c . . 
            . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
            c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
            f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
            f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
            f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
            . f 6 1 1 1 1 1 6 6 6 6 c . . . 
            . . f f c c c c c c c c . . . .
    """),
    SpriteKind.enemy)
setFrame()
controller.set_repeat_default(200, 200)
game.set_dialog_cursor(img("""
    ........................
        .....ffff...............
        ...fff22fff.............
        ..fff2222fff............
        .fffeeeeeefff...........
        .ffe222222eef...........
        .fe2ffffff2ef...........
        .ffffeeeeffff...........
        ffefbf44fbfeff..........
        fee41fddf14eef..........
        .ffffdddddeef...........
        fddddf444eef............
        fbbbbf2222f4e...........
        fbbbbf2222fd4...........
        .fccf45544f44...........
        ..ffffffff..............
        ....ff..ff..............
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
        ........................
"""))
game.show_long_text("Fight fire with ice!  Use your Icelandic sword to fight the fire snake! Chill him with your snow power and you will turn his fire to ice.  Collect the ice for points and collect the bonus items!  You will need them!",
    DialogLayout.BOTTOM)
game.show_long_text("Shoot with B (X on the keyboard). Hold down for rapid fire.",
    DialogLayout.BOTTOM)
myHealthBar = sprites.create(image.create(40, 4), SpriteKind.ArmorBar)
myHealthBar.set_position(0, -2)
myHealthBar.z = 1
maxHealth = 1
currHealth = maxHealth
targetHealth = maxHealth
fillHealthBar(myHealthBar, maxHealth, currHealth)
# END health bar

def on_on_update():
    if controller.right.is_pressed() and controller.down.is_pressed():
        mySprite.set_velocity(50, 50)
    elif controller.left.is_pressed() and controller.down.is_pressed():
        mySprite.set_velocity(-50, 50)
    elif controller.right.is_pressed() and controller.up.is_pressed():
        mySprite.set_velocity(50, -50)
    elif controller.left.is_pressed() and controller.up.is_pressed():
        mySprite.set_velocity(-50, -50)
    elif controller.right.is_pressed():
        mySprite.set_velocity(50, 0)
    elif controller.left.is_pressed():
        mySprite.set_velocity(-50, 0)
    elif controller.up.is_pressed():
        mySprite.set_velocity(0, -50)
    elif controller.down.is_pressed():
        mySprite.set_velocity(0, 50)
    else:
        mySprite.set_velocity(0, 0)
game.on_update(on_on_update)

def on_update_interval():
    global maxFrozen, vyEnemy, bFrozen, firePower, firePower2, firePower3, fireballPower
    if bFrozen:
        if maxFrozen <= 1000:
            maxFrozen += 500
        else:
            vyEnemy = vyPrevEnemy
            enemySprite.set_velocity(0, vyEnemy)
            enemySprite.start_effect(effects.fire, 1000)
            bFrozen = 0
            animation.run_image_animation(enemySprite, enemyFrames, 50, True)
    else:
        firePower = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . 4 4 4 4 4 4 4 . . . . . . 
                            . . 4 8 2 2 2 2 2 5 4 . . . . . 
                            . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                            4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                            4 4 4 2 2 4 4 4 2 2 4 4 4 4 4 . 
                            4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                            . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                            . . 4 8 2 2 2 2 2 5 4 . . . . . 
                            . . . 4 4 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            enemySprite,
            randint(-100, -5),
            0)
        firePower.set_kind(SpriteKind.enemyProjectile)
        if bDoublePower:
            firePower2 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . 4 4 4 4 4 4 4 . . . . . . 
                                    . . 4 8 2 2 2 2 2 5 4 . . . . . 
                                    . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                                    4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                                    4 4 4 2 2 4 4 4 2 2 4 4 4 4 4 . 
                                    4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                                    . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                                    . . 4 8 2 2 2 2 2 5 4 . . . . . 
                                    . . . 4 4 4 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                enemySprite,
                randint(-100, -5),
                15)
            firePower2.set_kind(SpriteKind.enemyProjectile)
        if bTriplePower:
            firePower3 = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . 4 4 4 4 4 4 4 . . . . . . 
                                    . . 4 8 2 2 2 2 2 5 4 . . . . . 
                                    . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                                    4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                                    4 4 4 2 2 4 4 4 2 2 4 4 4 4 4 . 
                                    4 4 4 8 2 2 4 2 2 5 4 4 4 4 . . 
                                    . 4 4 8 8 2 2 2 5 5 4 4 . . . . 
                                    . . 4 8 2 2 2 2 2 5 4 . . . . . 
                                    . . . 4 4 4 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                enemySprite,
                randint(-100, -5),
                -15)
            firePower3.set_kind(SpriteKind.enemyProjectile)
        if bESpecialPower:
            fireballPower = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . 4 4 4 5 5 4 4 4 . . . . 
                                    . . . 3 3 3 3 4 4 4 4 4 4 . . . 
                                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
                                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
                                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
                                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
                                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
                                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
                                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
                                    . . . 4 2 2 2 2 2 2 2 2 4 . . . 
                                    . . . . 4 4 2 2 2 2 4 4 . . . . 
                                    . . . . . . 4 4 4 4 . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                enemySprite,
                randint(-100, -5),
                -15)
            fireballPower.set_kind(SpriteKind.specialEProjectile)
            fireballPower.follow(mySprite)
game.on_update_interval(msTimer, on_update_interval)

def on_update_interval2():
    sendHealth()
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    if Math.percent_chance(40):
        createCloud()
game.on_update_interval(1000, on_update_interval3)

def on_update_interval4():
    sendBonus()
game.on_update_interval(1500, on_update_interval4)

def on_forever():
    if Math.percent_chance(60):
        createTree()
        if Math.percent_chance(50):
            pause(randint(150, 300))
            createTree()
    pause(1500)
forever(on_forever)

def on_update_interval5():
    global grass
    if Math.percent_chance(40):
        grass = sprites.create_projectile_from_side(grassImages[randint(0, len(grassImages) - 1)], -50, 0)
        grass.bottom = 115
        grass.z = -1
        grass.set_kind(SpriteKind.Bkgrd)
game.on_update_interval(200, on_update_interval5)
