namespace SpriteKind {
    export const heroProjectile = SpriteKind.create()
    export const enemyProjectile = SpriteKind.create()
    export const specialEProjectile = SpriteKind.create()
    export const specialHProjectile = SpriteKind.create()
    export const Bonus = SpriteKind.create()
    export const Health = SpriteKind.create()
    export const heroIceProjectile = SpriteKind.create()
    export const Helper = SpriteKind.create()
    export const Bkgrd = SpriteKind.create()
}
sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    vyEnemy = 50
    sprite.setPosition(140, randint(0, 115))
    sprite.setVelocity(0, vyEnemy)
    sprite.setFlag(SpriteFlag.BounceOnWall, true)
})
sprites.onOverlap(SpriteKind.enemyProjectile, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy()
    hitPlayer()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    playerframes,
    50,
    false
    )
    snowAmmo = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 75, 0)
    music.pewPew.play()
    snowAmmo.setKind(SpriteKind.Projectile)
    if (bIceAmmo) {
        iceAmmo = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 90, 0)
        iceAmmo.setKind(SpriteKind.heroIceProjectile)
    }
    if (bHSpecialAmmo) {
        freezeAmmo = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 80, 0)
        freezeAmmo.setKind(SpriteKind.specialHProjectile)
    }
    if (bDoubleHAmmo) {
        snowAmmo2 = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 75, 20)
        snowAmmo2.setKind(SpriteKind.Projectile)
    }
    if (bTripleHAmmo) {
        snowAmmo3 = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 75, -20)
        snowAmmo3.setKind(SpriteKind.Projectile)
    }
})
function hitPlayer () {
    if (hitDamage == -0.5 && ctrDamage < maxArmor) {
        ctrDamage += 1
        music.playTone(294, music.beat(BeatFraction.Sixteenth))
        music.playTone(387, music.beat(BeatFraction.Sixteenth))
        music.playTone(584, music.beat(BeatFraction.Sixteenth))
    } else {
        music.powerDown.play()
        info.changeLifeBy(-1)
        ctrDamage = 0
        // skip
        if (bTripleHAmmo) {
            bTripleHAmmo = 0
            bTripleBonus = 0
        } else if (bDoubleHAmmo) {
            bDoubleHAmmo = 0
            bDoubleBonus = 0
        } else if (bIceAmmo) {
            bIceAmmo = 0
            bIceBonus = 0
        }
    }
    if (info.life() == 0) {
        game.over(false)
    }
}
function sendBonus () {
    if (Math.percentChance(0.1)) {
            createBonusShip()
            bCreateHealthShip = 0
            bNeedHealth = 0
            bNeedBonus = 1
    }
    if (bCreateBonusShip) {
        if (bTripleBonus) {
            armorBonus = sprites.createProjectileFromSprite(img`
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
                `, shipSprite, 0, 10)
            armorBonus.setKind(SpriteKind.Bonus)
        } else if (bDoubleBonus) {
            snowAmmo3 = sprites.createProjectileFromSprite(img`
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
                `, shipSprite, 0, 10)
            snowAmmo3.setKind(SpriteKind.Bonus)
        } else if (bIceBonus) {
            snowAmmo2 = sprites.createProjectileFromSprite(img`
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
                `, shipSprite, 0, 10)
            snowAmmo2.setKind(SpriteKind.Bonus)
        } else {
            iceAmmo = sprites.createProjectileFromSprite(img`
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
                `, shipSprite, 0, 10)
            iceAmmo.setKind(SpriteKind.Bonus)
        }
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.specialEProjectile, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Health, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy()
    getHealth()
})
function createBonusShip () {
    shipSprite = sprites.create(img`
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
        `, SpriteKind.Helper)
    shipSprite.setPosition(160, 10)
    shipSprite.setVelocity(-26, 0)
    shipSprite.setFlag(SpriteFlag.DestroyOnWall, true)
    animation.runImageAnimation(
    shipSprite,
    shipFrames,
    50,
    true
    )
    bCreateBonusShip = 1
}
function createHealthShip () {
    shipSprite = sprites.create(img`
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
        `, SpriteKind.Helper)
    shipSprite.setPosition(160, 10)
    shipSprite.setVelocity(-26, 0)
    shipSprite.setFlag(SpriteFlag.DestroyOnWall, true)
    animation.runImageAnimation(
    shipSprite,
    shipFrames,
    50,
    true
    )
    bCreateHealthShip = 1
}
sprites.onOverlap(SpriteKind.Bonus, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy()
    getBonus()
})
function createCloud () {
    cloud = sprites.createProjectileFromSide(clouds[randint(0, clouds.length - 1)], -30, 0)
    cloud.bottom = randint(30, 55)
    cloud.z = -2
    cloud.setKind(SpriteKind.Bkgrd)
}
sprites.onOverlap(SpriteKind.heroIceProjectile, SpriteKind.enemyProjectile, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.enemyProjectile, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.specialHProjectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    if (bFrozen == 0) {
        animation.stopAnimation(animation.AnimationTypes.All, enemySprite)
        bFrozen = 1
        if (vyEnemy > 0) {
            vyPrevEnemy = vyEnemy
        }
        vyEnemy = 0
        otherSprite.setVelocity(0, vyEnemy)
        otherSprite.startEffect(effects.blizzard, 2000)
        bHSpecialAmmo = 0
        maxFrozen = 0
    }
})
function getBonus () {
    bCreateBonusShip = 0
    if (bNeedBonus) {
        music.playMelody("E E G - G G B C5 ", 480)
        if (bTripleBonus) {
            hitDamage = -0.5
            maxArmor += 1
            game.showLongText("You got " + (maxArmor+1) + " hit armor!", DialogLayout.Bottom)
        } else if (bDoubleBonus) {
            bTripleBonus = 1
            bTripleHAmmo = 1
            game.showLongText("You got triple ammo!  Try not to get hit or you will lose it!", DialogLayout.Bottom)
        } else if (bIceBonus) {
            bDoubleBonus = 1
            bDoubleHAmmo = 1
            game.showLongText("You got double ammo! Try not to get hit or you will lose it!", DialogLayout.Bottom)
        } else {
            bIceBonus = 1
            bIceAmmo = 1
            game.showLongText("You got ice ammo! Try not to get hit or you will lose it!", DialogLayout.Bottom)
        }
    }
    bNeedBonus = 0
}
function getHealth () {
    bCreateHealthShip = 0
    if (bNeedHealth) {
        music.powerUp.play()
        info.changeLifeBy(1)
    }
    bNeedHealth = 0
}
function sendHealth () {
    if(Math.percentChance(0.1)) {
            createHealthShip()
            bCreateBonusShip = 0
            bNeedBonus = 0
            bNeedHealth = 1
    }
    if(bCreateHealthShip){
        healthBonus = sprites.createProjectileFromSprite(img`
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
            `, shipSprite, 0, 10)
        healthBonus.setKind(SpriteKind.Health)
    }
}
sprites.onOverlap(SpriteKind.heroProjectile, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy()
    music.playTone(494, music.beat(BeatFraction.Sixteenth))
    music.playTone(587, music.beat(BeatFraction.Sixteenth))
    music.playTone(784, music.beat(BeatFraction.Sixteenth))
    info.changeScoreBy(1)
    if (info.score() % 20 == 0) {
        info.changeLifeBy(1)
        if (bFrozen) {
            vyEnemy += 0
        } else {
            if (vyEnemy >= 10 && vyEnemy <= 80) {
                vyEnemy += randint(-10, 10)
            } else {
                vyEnemy = randint(10, 80)
            }
        }
        if (msTimer > minTimer) {
            msTimer += -100
        }
        bHSpecialAmmo = 1
    }
    if (info.score() >= 80) {
        bDoubleAmmo = 1
    }
    if (info.score() >= 100) {
        bTripleAmmo = 1
    }
    if (info.score() >= 150) {
        bESpecialAmmo = 1
    }
})
sprites.onOverlap(SpriteKind.Bonus, SpriteKind.enemyProjectile, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Health, SpriteKind.enemyProjectile, function (sprite, otherSprite) {
    sprite.destroy()
})
function setFrame () {
    playerframes = [sprites.castle.heroSideAttackRight4, sprites.castle.heroSideAttackRight3, sprites.castle.heroSideAttackRight2, sprites.castle.heroSideAttackRight1, sprites.castle.heroSideAttackRight4]
    animation.runImageAnimation(
    mySprite,
    playerframes,
    50,
    false
    )
    enemyFrames = [
    sprites.builtin.forestSnake0,
    sprites.builtin.forestSnake1,
    sprites.builtin.forestSnake2,
    sprites.builtin.forestSnake3,
    sprites.builtin.forestSnake4,
    sprites.builtin.forestSnake5,
    sprites.builtin.forestSnake6,
    sprites.builtin.forestSnake7
    ]
    animation.runImageAnimation(
    enemySprite,
    enemyFrames,
    50,
    true
    )
    shipFrames = [sprites.space.spaceRedShip, sprites.space.spaceOrangeShip, sprites.space.spacePinkShip, sprites.space.spaceBlueShip, sprites.space.spaceGreenShip]
    clouds = [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `]
    trees = [img`
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
        `, img`
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
        `, img`
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
        `]
    grassImages = [
    img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . b . . . 
        . . . . b . . . 
        . . . b b . . . 
        . . . b b . . . 
        `,
    img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . b . . . . 
        . . . b . . . . 
        . . . b b . b . 
        . . . b b . b . 
        `,
    img`
        . . . . . . . . 
        . . . . . . . . 
        b . . . . . . . 
        b . . b . . . . 
        b . . b b . . . 
        b . b b b . . . 
        b . b b b . b . 
        b b b b b . b . 
        `,
    img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . b 
        . . . b . . . b 
        . . . b . . . b 
        . . . b b . b b 
        . . . b b . b b 
        `,
    img`
        . . . . . . . . 
        . . . . . . . . 
        . . . b . . . . 
        . . . b . . . . 
        . . b b . . . . 
        . . b b b . . . 
        . . b b b . . . 
        . . b b b . . . 
        `,
    img`
        . . . . . . . . 
        . . . . . . . . 
        . . . . . . . . 
        . b . . . . . . 
        . b . . . . . . 
        . b b . . . b . 
        . b b . . . b . 
        . b b . . . b . 
        `
    ]
}
sprites.onOverlap(SpriteKind.specialEProjectile, SpriteKind.heroProjectile, function (sprite, otherSprite) {
    otherSprite.destroy()
})
sprites.onOverlap(SpriteKind.specialEProjectile, SpriteKind.Player, function (sprite, otherSprite) {
    sprite.destroy()
    hitPlayer()
})
sprites.onOverlap(SpriteKind.Bonus, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.heroIceProjectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onCreated(SpriteKind.Player, function (sprite) {
    sprite.setFlag(SpriteFlag.StayInScreen, true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    fireAmmo.setImage(img`
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
        `)
    fireAmmo.setKind(SpriteKind.heroProjectile)
})
function createTree () {
    tree = sprites.createProjectileFromSide(trees[randint(0, trees.length - 1)], -50, 0)
    tree.bottom = 100
    tree.z = -1
    tree.setKind(SpriteKind.Bkgrd)
}
let grass: Sprite = null
let missleAmmo: Sprite = null
let fireAmmo3: Sprite = null
let fireAmmo2: Sprite = null
let tree: Sprite = null
let fireAmmo: Sprite = null
let grassImages: Image[] = []
let trees: Image[] = []
let enemyFrames: Image[] = []
let bESpecialAmmo = 0
let bTripleAmmo = 0
let bDoubleAmmo = 0
let healthBonus: Sprite = null
let maxFrozen = 0
let maxArmor = 0
let vyPrevEnemy = 0
let bFrozen = 0
let clouds: Image[] = []
let cloud: Sprite = null
let shipFrames: Image[] = []
let shipSprite: Sprite = null
let armorBonus: Sprite = null
let bNeedBonus = 0
let bNeedHealth = 0
let bCreateBonusShip = 0
let bCreateHealthShip = 0
let bIceBonus = 0
let bDoubleBonus = 0
let bTripleBonus = 0
let ctrDamage = 0
let snowAmmo3: Sprite = null
let bTripleHAmmo = 0
let snowAmmo2: Sprite = null
let bDoubleHAmmo = 0
let freezeAmmo: Sprite = null
let bHSpecialAmmo = 0
let iceAmmo: Sprite = null
let bIceAmmo = 0
let snowAmmo: Sprite = null
let playerframes: Image[] = []
let vyEnemy = 0
let enemySprite: Sprite = null
let mySprite: Sprite = null
let hitDamage = 0
let msTimer = 0
let minTimer = 0
game.splash("Fire & Ice")
minTimer = 200
msTimer = 1000
hitDamage = -1
info.setLife(5)
scene.setBackgroundImage(img`
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
    `)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
enemySprite = sprites.create(img`
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
    `, SpriteKind.Enemy)
setFrame()
game.onUpdate(function () {
    if (controller.right.isPressed() && controller.down.isPressed()) {
        mySprite.setVelocity(50, 50)
    } else if (controller.left.isPressed() && controller.down.isPressed()) {
        mySprite.setVelocity(-50, 50)
    } else if (controller.right.isPressed() && controller.up.isPressed()) {
        mySprite.setVelocity(50, -50)
    } else if (controller.left.isPressed() && controller.up.isPressed()) {
        mySprite.setVelocity(-50, -50)
    } else if (controller.right.isPressed()) {
        mySprite.setVelocity(50, 0)
    } else if (controller.left.isPressed()) {
        mySprite.setVelocity(-50, 0)
    } else if (controller.up.isPressed()) {
        mySprite.setVelocity(0, -50)
    } else if (controller.down.isPressed()) {
        mySprite.setVelocity(0, 50)
    } else {
        mySprite.setVelocity(0, 0)
    }
})
game.onUpdateInterval(msTimer, function () {
    if (bFrozen) {
        if (maxFrozen <= 1000) {
            maxFrozen += msTimer
        } else {
            vyEnemy = vyPrevEnemy
            enemySprite.setVelocity(0, vyEnemy)
            enemySprite.startEffect(effects.fire, 1000)
            bFrozen = 0
            animation.runImageAnimation(
            enemySprite,
            enemyFrames,
            50,
            true
            )
        }
    } else {
        fireAmmo = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
            . . . 4 4 4 4 4 4 4 . . . . . . 
            . . 4 8 2 2 2 2 2 5 4 . . . . . 
            . . 4 8 8 2 2 2 5 5 4 . . . . . 
            . . 4 8 2 2 4 2 2 5 4 . . . . . 
            . . 4 2 2 4 4 4 2 2 4 . . . . . 
            . . 4 8 2 2 4 2 2 5 4 . . . . . 
            . . 4 8 8 2 2 2 5 5 4 . . . . . 
            . . 4 8 2 2 2 2 2 5 4 . . . . . 
            . . . 4 4 4 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, enemySprite, randint(-100, -5), 0)
        fireAmmo.setKind(SpriteKind.enemyProjectile)
        if (bDoubleAmmo) {
            fireAmmo2 = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . 4 4 4 4 4 4 4 . . . . . . 
                . . 4 8 2 2 2 2 2 5 4 . . . . . 
                . . 4 8 8 2 2 2 5 5 4 . . . . . 
                . . 4 8 2 2 4 2 2 5 4 . . . . . 
                . . 4 2 2 4 4 4 2 2 4 . . . . . 
                . . 4 8 2 2 4 2 2 5 4 . . . . . 
                . . 4 8 8 2 2 2 5 5 4 . . . . . 
                . . 4 8 2 2 2 2 2 5 4 . . . . . 
                . . . 4 4 4 4 4 4 4 . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, enemySprite, randint(-100, -5), 15)
            fireAmmo2.setKind(SpriteKind.enemyProjectile)
        }
        if (bTripleAmmo) {
            fireAmmo3 = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . 4 4 4 4 4 4 4 . . . . . . 
                . . 4 8 2 2 2 2 2 5 4 . . . . . 
                . . 4 8 8 2 2 2 5 5 4 . . . . . 
                . . 4 8 2 2 4 2 2 5 4 . . . . . 
                . . 4 2 2 4 4 4 2 2 4 . . . . . 
                . . 4 8 2 2 4 2 2 5 4 . . . . . 
                . . 4 8 8 2 2 2 5 5 4 . . . . . 
                . . 4 8 2 2 2 2 2 5 4 . . . . . 
                . . . 4 4 4 4 4 4 4 . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, enemySprite, randint(-100, -5), -15)
            fireAmmo3.setKind(SpriteKind.enemyProjectile)
        }
        if (bESpecialAmmo) {
            missleAmmo = sprites.createProjectileFromSprite(img`
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
                `, enemySprite, randint(-100, -5), -15)
            missleAmmo.setKind(SpriteKind.specialEProjectile)
            missleAmmo.follow(mySprite)
        }
    }
    sendBonus()
})
game.onUpdateInterval(1000, function () {
    if (Math.percentChance(40)) {
        createCloud()
    }
})
game.onUpdateInterval(1500, function () {
    sendHealth()
})
forever(function () {
    if (Math.percentChance(60)) {
        createTree()
        if (Math.percentChance(50)) {
            pause(randint(150, 300))
            createTree()
        }
    }
    pause(1500)
})
game.onUpdateInterval(200, function () {
    if (Math.percentChance(40)) {
        grass = sprites.createProjectileFromSide(grassImages[randint(0, grassImages.length - 1)], -50, 0)
        grass.bottom = 115
        grass.z = -1
        grass.setKind(SpriteKind.Bkgrd)
    }
})
