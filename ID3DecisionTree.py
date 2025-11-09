import math
from collections import Counter, defaultdict

class ID3DecisionTree:
    def __init__(self):
        self.tree = None

    def entropy(self, data):
        labels = [row[-1] for row in data]
        counts = Counter(labels)
        total = len(data)
        return -sum((count/total) * math.log2(count/total) for count in counts.values())

    def info_gain(self, data, attr_index):
        total_entropy = self.entropy(data)
        values = defaultdict(list)
        for row in data:
            values[row[attr_index]].append(row)
        subset_entropy = sum((len(v)/len(data)) * self.entropy(v) for v in values.values())
        return total_entropy - subset_entropy

    def best_attribute(self, data):
        attrs = range(len(data[0]) - 1)
        gains = {a: self.info_gain(data, a) for a in attrs}
        return max(gains, key=gains.get)

    def fit(self, data, attributes):
        labels = [row[-1] for row in data]
        if len(set(labels)) == 1:
            return labels[0]
        if len(attributes) == 0:
            return Counter(labels).most_common(1)[0][0]

        best = self.best_attribute(data)
        tree = {attributes[best]: {}}
        for value in set(row[best] for row in data):
            subset = [row for row in data if row[best] == value]
            if not subset:
                tree[attributes[best]][value] = Counter(labels).most_common(1)[0][0]
            else:
                new_attrs = attributes[:best] + attributes[best+1:]
                new_data = [row[:best] + row[best+1:] for row in subset]
                tree[attributes[best]][value] = self.fit(new_data, new_attrs)
        self.tree = tree
        return tree
