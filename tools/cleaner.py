class DataCleaner:
    def __init__(self): self.rules = []
    def add(self, fn): self.rules.append(fn)
    def clean(self, d):
        for r in self.rules: d = r(d)
        return d
    @staticmethod
    def dedup(data, key="text"):
        seen = set()
        return [d for d in data if d[key] not in seen and not seen.add(d[key])]
