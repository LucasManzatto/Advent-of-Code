class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.left is None:
                print(f"Insert {data} on {self.data}")
                self.left = Node(data)
            else:
                print(f"Insert {data} on {self.data}")
                self.right = Node(data)
        else:
            self.data = data

    def find_and_insert(self, node, data):
        print(f"Finding {node}")
        if self.left:
            if self.left.data == node:
                return self.left.insert(data)
            self.left.find_and_insert(node, data)
        if self.right:
            if self.right.data == node:
                return self.right.insert(data)
            self.right.find_and_insert(node, data)

    def count_all_paths(self):
        if self.left and self.right:
            return self.left.count_paths() + self.right.count_paths() + 1
        if self.left:
            return self.left.count_paths() + 1
        if self.right:
            return self.right.count_paths() + 1
        if self.is_leaf():
            return 0

    def count_paths(self,counter =0):
        if self.left and self.right:
            return self.left.count_paths() + self.right.count_paths() + 1
        if self.left:
            return self.left.count_paths() + 1
        if self.right:
            return self.right.count_paths() + 1
        if self.is_leaf():
            return 1

    def is_leaf(self):
        return self.right is None and self.left is None

    def get_leaves(self):
        if self.left and self.right:
            return self.left.get_leaves() + self.right.get_leaves()
        if self.left:
            return self.left.get_leaves() + []
        if self.right:
            return self.right.get_leaves() + []
        if self.left is None and self.right is None:
            return [self.data]

    def get_distance(self,root,x):
        if root is None:
            return -1
        distance = -1
        if root.data == x:
            return distance + 1
        else:
            distance = root.get_distance(root.left,x)
            if distance >= 0:
                return distance + 1
            else:
                distance = root.get_distance(root.right,x)
                if distance >= 0:
                    return distance + 1
        
        return distance


    def PrintTree(self):
        print(f"\nNode:{self.data} ")
        if self.left:
            print(f"Left:{self.left.data}")
        if self.right:
            print(f"Right:{self.right.data}")

        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


input = open('input.txt').read().splitlines()

first_object, second_object = input[0].split(')')

root = Node(first_object)
root.insert(second_object)

letters =[first_object]

for obj in input[1:]:
    first_object, second_object = obj.split(')')
    letters.append(first_object)
    letters.append(second_object)
    root.find_and_insert(first_object, second_object)

letters = list(set(letters))
# print(letters)
root.PrintTree()
total_count =0
for letter in letters:
    total_count += root.get_distance(root,letter)
print(total_count)
# def count(node):
#     count =0
#     if node.left:
#         count += node.left.count_paths()
#     if node.right:
#         count += node.right.count_paths()
#     return count

# while not node.is_leaf():
#     total_count += count(node)
#     node = node.left
# print(total_count)
