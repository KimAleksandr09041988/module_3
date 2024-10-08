data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5}, # 11
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    res = 0
    if (isinstance(args, list)) or (isinstance(args, tuple)) or (isinstance(args, set)):
        for item in args:
            if isinstance(item, dict):
                values_ = item.values()
                keys_ = item.keys()
                res += calculate_structure_sum(*values_)
                res += calculate_structure_sum(*keys_)
            elif isinstance(item, str):
                res += len(item)
            elif isinstance(item, int):
                res += item
            else:
                res += calculate_structure_sum(*item)
    return res

result = calculate_structure_sum(data_structure)
print(result)