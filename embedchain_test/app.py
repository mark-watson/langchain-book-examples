
# https://github.com/embedchain/embedchain

from embedchain import App

test_chat = App()


def test(q):
    print(q)
    print(test_chat.query(q), "\n")

test("How can I iterate over a list in Haskell?")
test("How can I edit my Common Lisp files?")
test("How can I scrape a website using Common Lisp?")