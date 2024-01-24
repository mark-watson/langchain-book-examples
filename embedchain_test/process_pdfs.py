
# https://github.com/embedchain/embedchain

from embedchain import App
import os

test_chat = App()

my_books_dir = "/Users/markw/data/"

for filename in os.listdir(my_books_dir):
    if filename.endswith('.pdf'):
        print("processing filename:", filename)
        test_chat.add(os.path.join(my_books_dir, filename))

