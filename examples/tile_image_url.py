from wplace import Pixel

wplace_link = "https://wplace.live/?lat=52.53835814390717&lng=13.37545865302734"
pixel = Pixel.from_link(wplace_link)
print(f"Selected pixel: {pixel!r}.")

region = pixel.region
print(f"Lies within {region!r}. Coords within region: {pixel.region_pixel}.")
print(f"Navigate to region origin: {region.origin.link(select=True)}")

tile = pixel.tile
print(f"Lies within {tile!r}. Coords within tile: {pixel.tile_pixel}.")
print(f"Tile image URL: {tile.url}")
