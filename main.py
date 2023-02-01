def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.guard, SpriteKind.enemy, on_on_overlap)

def on_on_score():
    namor.destroy()
    scene.set_background_image(assets.image("""
        boston-bridge
    """))
    effects.confetti.start_screen_effect()
    shuri.say_text(":)", 2000, False)
info.on_score(20, on_on_score)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

namor: Sprite = None
shuri: Sprite = None
game.show_long_text("press w,a,s,d to move shuri", DialogLayout.FULL)
scene.set_background_image(assets.image("""
    boston-bridge
"""))
shuri = sprites.create(assets.image("""
    shuri
"""), SpriteKind.player)
controller.move_sprite(shuri)
shuri.set_stay_in_screen(True)
namor = sprites.create(assets.image("""
    namor
"""), SpriteKind.enemy)
namor.set_position(148, 2)
namor.follow(shuri, 30)
riri = sprites.create(assets.image("""
    riri
"""), SpriteKind.guard)
okoye = sprites.create(assets.image("""
    okoye
"""), SpriteKind.guard)
controller.move_sprite(riri, 34, -53)
controller.move_sprite(okoye, -68, -58)