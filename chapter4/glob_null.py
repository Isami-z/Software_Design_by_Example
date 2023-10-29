class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()

    def match(self, text, start=0):
        result = self._match(text, start)
        return result == len(text)


class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        return start
