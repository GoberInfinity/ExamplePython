class AhoNode:
    def __init__(self):
        self.goto = {}  # Transition
        self.out = []  # Points to the possible patterns occuring at that position
        self.fail = None  # Point to node which esssentially is the longest suffix


def aho_create_trie(patterns):
    root = AhoNode()

    for pattern in patterns:
        node = root
        for symbol in pattern:
            # Will insert key with a value default_value if key is not in the dictionary
            node = node.goto.setdefault(
                symbol, AhoNode()
            )  # Create the edge(transition)
        node.out.append(pattern)
    return root


def aho_create_statemachine(patterns):
    root = aho_create_trie(patterns)
    queue = []
    # All the vertex from root node, their longest suffix is root
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    # Construct suffix and output links in Breadth First Order.
    while len(queue) > 0:
        current_node = queue.pop(0)

        for (
            key,
            next_node,
        ) in current_node.goto.items():  # The vertex after the transition
            queue.append(next_node)
            fail_node = current_node.fail
            while fail_node != None and not key in fail_node.goto:
                fail_node = fail_node.fail
            next_node.fail = fail_node.goto[key] if fail_node else root
            next_node.out += next_node.fail.out

    return root


def aho_find_all(text, root, callback):
    node = root

    # If current character matches any of children then follow it
    # otherwise follow the suffix link

    for current in range(len(text)):
        while node != None and not text[current] in node.goto:
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[text[current]]
        # At every node follow the output links
        # to get patterns occurring till the current position.
        for pattern in node.out:
            callback(current - len(pattern) + 1, pattern)


def on_occurence(pos, patterns):
    print(f"At pos {pos} found pattern: {patterns}")


patterns = ["a", "ab", "abc", "bc", "c", "cba"]
text = "abcba"
root = aho_create_statemachine(patterns)
aho_find_all(text, root, on_occurence)
