from pixel import Pixel
from image import Image
class Encoder:
    def __init__(self, img: Image, version=1):
        self.image = img
        self.version = version

    def save_to(self, path: str) -> None:
        with open(path, "wb") as file:
            file.write(b'ULBMP')

            if self.version == 1:
                file.write(bytes([1]))  # Version 1
                header_size = 12  # Taille de l'en-tête en octets
                file.write(self._int_to_bytes(header_size, 2))

                # Écrire les dimensions de l'image (largeur et hauteur)
                file.write(self._int_to_bytes(self.image.width, 2))
                file.write(self._int_to_bytes(self.image.height, 2))

                for pixel in self.image.pixels:
                    file.write(bytes([pixel.getRouge(), pixel.getGreen(), pixel.getBlue()]))
            elif self.version == 2:
                file.write(bytes([2]))  # Version 2
                header_size = 12  # Taille de l'en-tête en octets
                file.write(self._int_to_bytes(header_size, 2))

                # Écrire les dimensions de l'image (largeur et hauteur)
                file.write(self._int_to_bytes(self.image.width, 2))
                file.write(self._int_to_bytes(self.image.height, 2))
                list_pixels = self.image.pixels

                i = 0

                while i < len(list_pixels):
                    count = 1
                    while i + count < len(list_pixels) and count < 255 and list_pixels[i] == list_pixels[i + count]:
                        count += 1

                    file.write(bytes([count]))
                    pixel = list_pixels[i]
                    file.write(bytes([pixel.getRouge(), pixel.getGreen(), pixel.getBlue()]))

                    i += count

    def _int_to_bytes(self, n: int, length: int) -> bytes:
        return n.to_bytes(length, byteorder='little')

