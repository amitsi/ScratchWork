import random

class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class binSearchTree():

    def __init__(self):
        self.g_root = None
        self.spacer = 50
        self.inter_spacer = 3
        self.max_depth = 100
        self.max_nodes = 0

    def _add_to_tree(self, root, node):
        if not root:
            root = node
        elif node.val < root.val:
            root.left = self._add_to_tree(root.left, node)
        else:
            root.right = self._add_to_tree(root.right, node)
        return root

    def insert(self, val):
        n = Node(val)
        self.g_root = self._add_to_tree(self.g_root, n)

    def _get_slash(self, line):
        outp = ""
        for i in range(len(line)):
            if not line[i].isdigit():
                if line[i+1].isdigit():
                    outp += "/"
                    continue
                if i-1 >= 0:
                    if line[i-1].isdigit():
                        outp += "\\"
                        continue
            if line[i].isdigit():
                if i+1 >= len(line):
                    outp += " \\"
                    continue
            outp += " "
        return outp

    def _pprint(self, spacer, root, depth, show_arr):
        if depth >= self.max_depth:
            print("Exceeding max depth %s...Exiting." % self.max_depth)
            exit(0)
        if not show_arr[depth]:
            output = " "*spacer + str(root.val)
        else:
            diff = spacer-len(show_arr[depth])
            diff = 2 if diff <= 0 else diff
            output = " "*diff + str(root.val)
        show_arr[depth] += output
        if root.left:
            self._pprint(spacer-self.inter_spacer, root.left, depth+1, show_arr)
        if root.right:
            self._pprint(spacer+self.inter_spacer, root.right, depth+1, show_arr)

    def show(self):
        if not self.g_root:
            print("Tree is empty")
        else:
            show_arr = [""]*self.max_depth
            self._pprint(self.spacer, self.g_root, 0, show_arr)
            for line in show_arr:
                print(line + "\n" + self._get_slash(line))
                if not line: break

bst = binSearchTree()
uniquelist = []
while len(uniquelist) <= 50:
    val = int(random.random()*1000 % 100)
    if val not in uniquelist:
        uniquelist.append(val)

for val in uniquelist:
    bst.insert(val)
    print("Inserted value: %d" % val)
print("="*30)
bst.show()
print("="*30)
