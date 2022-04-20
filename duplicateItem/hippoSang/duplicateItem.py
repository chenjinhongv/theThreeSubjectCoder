import random


def find_duplicate_items(items):
    result = []
    seen_items = set()
    for item in items:
        if item in seen_items:
            result.append(item)
        seen_items.add(item)
    return set(result)


def find_duplicates_items_2(items):
    for i in range(len(items)):
        while items[i] != i:
            if items[items[i]] == items[i]:
                return items[i]
            else:
                temp = items[items[i]]
                items[items[i]] = items[i]
                items[i] = temp


if __name__ == "__main__":
    items = [random.randint(0, 10) for i in range(20)]
    print("items:", items)
    duplicate_items = find_duplicate_items(items)
    print("duplicate_items:", duplicate_items)
    items_2 = [random.randint(0, 9) for i in range(10)]
    print("items_2:", items_2)
    duplicate_item = find_duplicates_items_2(items_2)
    print("dupliate_item:", duplicate_item)
