import glob
from PIL import Image
filenames = glob.glob('128/emoji_*.png')
emojis = [filename[11:-4] for filename in filenames]

EMOJI_SIZE = 128

STYLE_TEMPLATE = '''.e{code} {{
	background: no-repeat url(http://chaosagent.io/emoji_spritemap.png) 0px, -{position}px !important;
	background-size: cover !important;
}}'''

image = Image.new('RGBA', (EMOJI_SIZE, EMOJI_SIZE * len(emojis)))
styles = []

for i, (filename, emoji) in enumerate(zip(filenames, emojis)):
	this_im = Image.open(filename)
	box = (0, EMOJI_SIZE * i, EMOJI_SIZE, EMOJI_SIZE * (i + 1))
	image.paste(this_im.crop((0, 0, EMOJI_SIZE, EMOJI_SIZE)), box)
	styles.append(STYLE_TEMPLATE.format(code=emoji, position=EMOJI_SIZE * i))

image.save('spritemap.png')

open('emoji_list.json', 'w').write(repr(emojis))
open('emojis.css', 'w').write('\n'.join(styles))

