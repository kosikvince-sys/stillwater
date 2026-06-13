# builds the Stillwater app icons, run once with python3 make_icons.py
import numpy as np
from PIL import Image

SIZE = 1024
cx, cy = SIZE / 2, SIZE / 2

y, x = np.mgrid[0:SIZE, 0:SIZE].astype(np.float64)
d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)

# deep water gradient, top left glow fading to near black
t = (x * 0.3 + y) / (SIZE * 1.3)
top = np.array([6, 34, 42], dtype=np.float64)
bot = np.array([3, 16, 20], dtype=np.float64)
img = top[None, None, :] * (1 - t[..., None]) + bot[None, None, :] * t[..., None]

# faint caustic pool of light behind everything
caustic = np.exp(-((d / (SIZE * 0.55)) ** 2)) * 14
img += caustic[..., None] * np.array([20, 60, 60]) / 60

# ripple rings, bright front fading as they travel outward
ring_color = np.array([200, 240, 235], dtype=np.float64)
for r, a, w in [(150, 0.55, 13), (265, 0.40, 12), (380, 0.28, 11), (490, 0.16, 10)]:
    band = np.exp(-(((d - r) / w) ** 2)) * a
    img = img * (1 - band[..., None]) + ring_color[None, None, :] * band[..., None]

# the wisp, warm white core with a teal halo
halo = np.exp(-((d / 130) ** 2)) * 0.55
img = img * (1 - halo[..., None]) + np.array([170, 240, 230])[None, None, :] * halo[..., None]
core = np.exp(-((d / 46) ** 2))
img = img * (1 - core[..., None]) + np.array([255, 255, 252])[None, None, :] * core[..., None]

out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), 'RGB')
out.save('icon-1024.png')
for size, name in [(512, 'icon-512.png'), (192, 'icon-192.png'), (180, 'apple-touch-icon.png')]:
    out.resize((size, size), Image.LANCZOS).save(name)
print('icons written')
