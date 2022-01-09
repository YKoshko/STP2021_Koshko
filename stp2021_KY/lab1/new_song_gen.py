from classes.crawler import crawler
from classes.generator import generator
from classes.saver import saver


dir, verse_size_1, verse_size_2, chorus_size = map(str, input('song directory, 2 verse and chorus sizes : ').split())

ex_crawl = crawler(dir)
ex_gen = generator(verse_size_1, verse_size_2, chorus_size)
ex_save = saver(ex_gen.lyrics_generation(ex_crawl.crawl_function()))
ex_save.saver_function()
