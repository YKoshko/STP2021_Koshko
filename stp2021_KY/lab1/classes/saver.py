class saver:

    def __init__(self, lyrics_list):
        self.lyrics_list = lyrics_list

    def saver_function(self):
        self.writer(2)
        self.writer(0)
        self.writer(2)
        self.writer(1)
        self.writer(2)

    def writer(self, num):
        with open('generated_song.txt', 'a', encoding='utf-8') as file:
            for lyric in self.lyrics_list[num]:
                file.write(lyric)
            file.write('\n\n')

