
# https://github.com/embedchain/embedchain

from embedchain import App
import os

test_chat = App()

my_books_dir = "/Users/markwatson/Library/Mobile Documents/com~apple~CloudDocs/Documents/my book PDFs/"

for filename in os.listdir(my_books_dir):
    if filename.endswith('.pdf'):
        print("processing filename:", filename)
        test_chat.add("pdf_file", os.path.join(my_books_dir, filename))

