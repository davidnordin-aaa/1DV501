import HashSet as hset
import BstMap as bst


def read_words(path):
    lst = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            lst.append(word)
    return lst


def unique_words(file):
    text = hset.HashSet()
    text.init()
    with open(file, 'r', encoding='utf-8') as file:
        data = file.read()
        words = data.split()
        for word in words:
            text.add(word)
    bucket = text.bucket_list_size()
    max = text.max_bucket_size()
    z_b_r = text.zero_bucket_ratio()
    print("Hashing-stats")
    print(f"Bucket list size: {bucket}")
    print(f"Max bucket size: {max}")
    print(f"Zero bucket ratio: {z_b_r}")
    return text.get_size()


def top_ten(words):
    leafs = bst_map.count_leafs()
    size = bst_map.size()
    max = bst_map.max_depth()
    for word in words:
        bst_words = bst_map.get(word)
        if len(word) > 4:
            if bst_words is not None:
                bst_map.put(word, bst_words + 1)
            else:
                bst_map.put(word, 1)
    print("BST-stats")
    print(f"max depth: {max}")
    print(f"Leaf count: {leafs}")
    print(f"number of nodes: {size}")
    sort_value = sorted(bst_map.as_list(), key=lambda v: v[1], reverse=True)
    print("\nTop 10 words")
    for i in range(10):
        print((sort_value[i][0]), (sort_value[i][1]))
    return ""


#  change path
path = "files/brian.txt"
# path = "files/swenews.txt"

unique = unique_words(path)
print(f"Unique: {unique}\n")

bst_map = bst.BstMap()

readwords = read_words(path)
for i in readwords:
    bst_map.put(i, 0)

top10 = top_ten(readwords)

for x, y in top10:
    print(f"{x} {y}\n")
