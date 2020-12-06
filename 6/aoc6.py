from collections import Counter


class ResponseProcessor:
    def process(self, file):
        with open(file) as file:
            for line in file:
                line = line.strip()
                if not line:
                    self.after_group()
                else:
                    self.process_line(line)
            self.after_group()
        return self.get_results()


class UniqueResponseProcessor(ResponseProcessor):
    groups = []
    current_group = set()

    def after_group(self):
        self.groups.append(self.current_group)
        self.current_group = set()

    def process_line(self, line):
        self.current_group.update(c for c in line)

    def get_results(self):
        return sum(len(g) for g in self.groups)


class UnanimousResponseProcessor(ResponseProcessor):
    total = 0
    current_group_count = 0
    current_group_resp = []

    def after_group(self):
        count = Counter(self.current_group_resp)
        self.total += len([k for k,v in count.items() if v == self.current_group_count])
        self.current_group_count = 0
        self.current_group_resp = []

    def process_line(self, line):
        self.current_group_count += 1
        self.current_group_resp.extend(c for c in line.strip())

    def get_results(self):
        return self.total


p1 = UniqueResponseProcessor().process('answers.txt')
p2 = UnanimousResponseProcessor().process('answers.txt')

print('Part 1:', p1)
assert p1 == 6506

print('Part 2:', p2)
assert p2 == 3243
