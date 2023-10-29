from glob_null import Null


class Matchers:
    def __init__(self):
        self.matchers = []
        self.rest = Null()

    def add(self, match):
        self.matchers.append(match)

    def build(self):
        for item in reversed(self.matchers):
            print(item)
            item.rest = self.rest
            self.rest = item
        print(self.rest)

    def match(self, text):
        return self.rest.match(text)
