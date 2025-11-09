from ID3DecisionTree import ID3DecisionTree
data = [
    ['>=35', 'hoch', 'Abitur', 'O'],
    ['<35', 'niedrig', 'Master', 'O'],
    ['>=35', 'hoch', 'Bachelor', 'M'],
    ['>=35', 'niedrig', 'Abitur', 'M'],
    ['>=35', 'hoch', 'Master', 'O'],
    ['<35', 'hoch', 'Bachelor', 'O'],
    ['<35', 'niedrig', 'Abitur', 'M'],
]
attributes = ['Alter', 'Einkommen', 'Bildung']

tree = ID3DecisionTree()
decision_tree = tree.fit(data, attributes)
print(decision_tree)
