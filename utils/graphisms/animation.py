import pygame.image

from utils.graphisms import Tileset


class Animation(Tileset):
    def __init__(self, file, n_frames, factor=10):
        self.n_frames = n_frames

        super().__init__(file, factor=factor)
        self.size = self.rect.size[0]/n_frames, self.rect.size[1]

    def load_all(self):
        for i in range(self.n_frames):
            self.load_frame(i, (i, 0))
            # print("loading", i)
            # pygame.image.save(self.get_frame(i), "test_"+str(i)+".png")

    def load_frame(self, index, position, rotation=0):
        return super().load_tile(index, position, rotation)

    def get_animation(self):
        return [self.tile_repertoire.get(frame) for frame in sorted(self.tile_repertoire.keys())]

    def get_frame(self, index):
        return super().get_texture(index)

    def get_frame_num(self):
        return self.n_frames
