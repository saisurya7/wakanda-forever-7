sprites.onOverlap(SpriteKind.Guard, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.showLongText("When game begins, press the ARROW KEYS to move Shuri, Okoye and Riri. If Namor catches you, you will lose points! ", DialogLayout.Full)
    info.changeScoreBy(1)
    namor.setPosition(148, 2)
})
info.onScore(20, function () {
    namor.destroy()
    scene.setBackgroundImage(assets.image`boston-bridge`)
    effects.confetti.startScreenEffect()
    shuri.sayText(":)", 2000, false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    namor.setPosition(148, 2)
})
let namor: Sprite = null
let shuri: Sprite = null
scene.setBackgroundImage(assets.image`boston-bridge`)
shuri = sprites.create(assets.image`shuri`, SpriteKind.Player)
controller.moveSprite(shuri)
shuri.setStayInScreen(true)
namor = sprites.create(assets.image`namor`, SpriteKind.Enemy)
namor.setPosition(148, 2)
namor.follow(shuri, 30)
let riri = sprites.create(assets.image`riri`, SpriteKind.Guard)
let okoye = sprites.create(assets.image`okoye`, SpriteKind.Guard)
controller.moveSprite(riri, 34, -53)
controller.moveSprite(okoye, -68, -58)
