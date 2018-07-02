import glob
from PIL import Image
filenames = glob.glob('128/emoji_*.png')
emojis = [filename[11:-4] for filename in filenames]

EMOJI_SIZE = 128
ROW_WIDTH = 255

STYLE_TEMPLATE = '''.e{code} {{
	background: no-repeat url(https://github.com/chaosagent/hangouts_emojis/raw/master/spritemap.png) -{pos_x}px, -{pos_y}px !important;
	background-size: {size_x}px {size_y}px !important;
}}'''

image = Image.new('RGBA', (EMOJI_SIZE * ROW_WIDTH, EMOJI_SIZE * (len(emojis) // ROW_WIDTH + (1 if len(emojis) % ROW_WIDTH else 0))))
styles = []

DISPLAY_SIZE = 48

for i, (filename, emoji) in enumerate(zip(filenames, emojis)):
	this_im = Image.open(filename)
	left = EMOJI_SIZE * (i % ROW_WIDTH)
	top = EMOJI_SIZE * (i // ROW_WIDTH)
	box = (left, top, left + EMOJI_SIZE, top + EMOJI_SIZE)
	image.paste(this_im.crop((0, 0, EMOJI_SIZE, EMOJI_SIZE)), box)
	styles.append(STYLE_TEMPLATE.format(
		code=emoji,
		pos_x=left * DISPLAY_SIZE // EMOJI_SIZE,
		pos_y=top * DISPLAY_SIZE // EMOJI_SIZE,
		size_x=image.size[0] * DISPLAY_SIZE // EMOJI_SIZE,
		size_y=image.size[0] * DISPLAY_SIZE // EMOJI_SIZE,
	))

image.save('spritemap.png')

open('emoji_list.json', 'w').write(repr(emojis))
open('emojis.css', 'w').write('\n'.join(styles))

