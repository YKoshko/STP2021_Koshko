from random import choice


class generator:

    def __init__(self, verse_size_1, verse_size_2, chorus_size):
        self.verse_size_1 = verse_size_1
        self.verse_size_2 = verse_size_2
        self.chorus_size = chorus_size

    def lyrics_generation(self, rows_list):
        self.verse_1_list = [choice(rows_list) for i in range(int(self.verse_size_1))]
        self.verse_2_list = [choice(rows_list) for i in range(int(self.verse_size_2))]
        self.chorus_size = [choice(rows_list) for i in range(int(self.chorus_size))]
        return [self.verse_1_list, self.verse_2_list, self.chorus_size]
