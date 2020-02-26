import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create a sprite
img = pyglet.image.load('assets/hero/sliced/idle-1.png')
spr = pyglet.sprite.Sprite(img, x = 100, y = 200)
spr.scale = 4

keys = pyglet.window.key.KeyStateHandler()
win.push_handlers(keys)

def update(dt):
  if keys[pyglet.window.key.LEFT]:
    spr.x -= 1
if keys[pyglet.window.key.RIGHT]:
  spr.x += 1

# Start the event loop
@window.event
def on_draw():
    window.clear()
    spr.draw()


pyglet.app.run()
