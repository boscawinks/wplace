from wplace import Pixel, WplaceAPI

api = WplaceAPI()

wplace_link = "https://wplace.live/?lat=52.53835814390717&lng=13.37545865302734"
pixel = Pixel.from_link(wplace_link)
print(f"Selected pixel: {pixel!r}.")
pixel_info = api.fetch_pixel_info(pixel=pixel)
print(f"Pixel info: {pixel_info}")

region = pixel.region
print(f"Lies within {region!r}. Coords within region: {pixel.coords_in_region}.")
link = api.get_pixel_link(region.origin, select=True)
print(f"Navigate to region origin: {link}")

tile = pixel.tile
print(f"Lies within {tile!r}. Coords within tile: {pixel.coords_in_tile}.")
img_url = api.get_tile_url(tile)
print(f"Tile image URL: {img_url}")
chunk = api.fetch_tile_image(tile=tile)
chunk.show()
