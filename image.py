from pixel import Pixel
class Image:
    def __init__(self, width: int, height: int, pixels: list[Pixel]):
        if len(pixels) != width * height:
            raise ValueError("La liste des pixels doit avoir une taille egale a width * height")
        self.width = width
        self.height = height
        self.pixels = pixels

    def __getitem__(self, pos: tuple[int, int]) -> Pixel:
        x, y = pos
        index = x * self.width + y
        if index >= 0 and (index < self.width * self.height):
            return self.pixels[index]
        else:
            raise IndexError("La position n'est pas valide dans l'image")

    def __setitem__(self, pos: tuple[int, int], pix: Pixel) -> None:
        x, y = pos
        index = x * self.width + y
        if index >= 0 and (index < self.width * self.height):
            self.pixels[index] = pix
        else:
            raise IndexError("La position n'est pas valide dans l'image")

    def __eq__(self, other: 'Image') -> bool:
        if not isinstance(other, Image):
            return False
        return self.width == other.width and self.height == other.height and self.pixels == other.pixels

