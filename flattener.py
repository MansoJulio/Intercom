class Flattener:
    def __init__(self):
        pass

    @staticmethod
    def flatten(the_list):
        flat_list = []
        if the_list is None:
            return None
        if not isinstance(the_list, list):
            raise TypeError("Input is expected to be a list")
        for item in the_list:
            if isinstance(item, list):
                flat_list += Flattener.flatten(item)
            elif isinstance(item, int):
                flat_list.append(item)
            else:
                raise TypeError("All items in the input should be integers or nested lists of integers")
        return flat_list


details = [[1, 2], 3, [4, [5, [6], 7]], 8, [9, [10], 11], 12, [13, [14, [15, [16]]]]]
flattened = Flattener.flatten(details)
print (flattened)

