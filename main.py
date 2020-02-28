import pyglet # import the library
import random
import time
win = pyglet.window.Window() # create the window


x = 200
y = 200



# Create a sprite
img = pyglet.image.load('assets/hero/sliced/idle-1.png')
spr = pyglet.sprite.Sprite(img, x = 100, y = 200)
spr.scale = 3

# create another image
img = pyglet.image.load('/Users/bkrive19/Downloads/WASD.gif')
smol_img = img.get_region(x=0, y=0, width=32, height=32)
spri = pyglet.sprite.Sprite(smol_img, x = 100, y = 100)
spri.scale = 4



#keys setup
keys = pyglet.window.key.KeyStateHandler()
win.push_handlers(keys)

#text
label = pyglet.text.Label('Move with W,A,S,D', x = 498, y = 467)


def update(dt):
  win.clear()

  if keys[pyglet.window.key.A]:
    spr.x -= 3
  if keys[pyglet.window.key.D]:
    spr.x += 3
  if keys[pyglet.window.key.S]:
    spr.y -= 3
  if keys[pyglet.window.key.W]:
    spr.scale = 3
    spr.y += 3

# Start the event loop
@win.event
def on_draw():
    win.clear()
    label.draw()
    spr.draw()


pyglet.clock.schedule(update) 
pyglet.app.run()
