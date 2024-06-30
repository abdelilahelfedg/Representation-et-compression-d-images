from pixel import Pixel
from image import Image
class Decoder:
    @staticmethod
    def load_from(path: str) -> Image:
        with open(path, 'rb') as file:
            # Lire et valider l'en-tête ULBMP
            header = file.read(12)
            if header[:5] != b'ULBMP':
                raise Exception("Format de fichier ULBMP invalide.")
            version = header[5]
            if version != 1 and version != 2:
                raise Exception(f"Version ULBMP {version} non prise en charge.")

            # Lire la taille de l'en-tête
            header_size = int.from_bytes(header[6:8], byteorder='little')

            # Lire les dimensions de l'image
            width = int.from_bytes(header[8:10], byteorder='little')
            height = int.from_bytes(header[10:12], byteorder='little')

            # Lire les pixels de l'image
            pixels = []
            if version == 1:
                while True:
                    byte = file.read(3)
                    if not byte:
                        break
                    pixels.append(Pixel(byte[0], byte[1], byte[2]))
            elif version == 2:
                while True:
                    block_size_byte = file.read(1)
                    if not block_size_byte:
                        break
                    block_size = block_size_byte[0]
                    color_bytes = file.read(3)
                    if len(color_bytes) != 3:
                        raise Exception("Unexpected end of file while reading pixel data.")
                    pixel = Pixel(color_bytes[0], color_bytes[1], color_bytes[2])
                    for _ in range(block_size):
                        pixels.append(pixel)

            # Vérifier si le nombre de pixels correspond à la taille de l'image
            if len(pixels) != width * height:
                raise Exception("Nombre de pixels invalide.")

            # Créer et retourner l'image
            return Image(width, height, pixels)

