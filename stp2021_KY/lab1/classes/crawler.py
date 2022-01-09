from os import listdir


class crawler:

    def __init__(self, dir):
        self.dir = dir
        self.songs_list = listdir(self.dir)
        self.rows_list = []

    def crawl_function(self):
        for song in self.songs_list:
            with open(self.dir + '\\' + song, 'r', encoding='utf-8') as file:
                for row in file:
                    self.rows_list.append(row)
        return self.rows_list
