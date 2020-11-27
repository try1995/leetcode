__all__ = ["TreeNode", "convert_list_to_tree", "LDR", "convert_list_to_node", "Node", "ListNode"]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


res = []


def convert_list_to_tree(ls: list) -> TreeNode:
    len_ls = len(ls)
    if len_ls == 0:
        return None
    all = []
    n = 0
    j = 0
    # 将list里面的元素转换为节点
    ls = [TreeNode(x) for x in ls]
    # 第一行有1个，第二层有两个，第三层有4个。。。加入到list里，最后一层叶子节点不需要存，因为循环的时候最后一层已经沒有叶子了
    while n + pow(2, j) < len_ls:
        all.append(ls[n: n + pow(2, j)])
        n = n + pow(2, j)
        j += 1

    # 保存头节点，从ls里面吧头节点删掉
    begin = ls.pop(0)
    for i in all:
        while len(i):
            if i[0].val:
                left = ls.pop(0)
                if left.val:
                    i[0].left = left
                right = ls.pop(0)
                if right.val:
                    i[0].right = right
            else:
                ls.pop(0)
                ls.pop(0)
            i.pop(0)
    return begin


def convert_list_to_node(ls: list) -> Node:
    len_ls = len(ls)
    if len_ls == 0:
        return None
    all = []
    n = 0
    j = 0
    # 将list里面的元素转换为节点
    ls = [TreeNode(x) for x in ls]
    # 第一行有1个，第二层有两个，第三层有4个。。。加入到list里，最后一层叶子节点不需要存，因为循环的时候最后一层已经沒有叶子了
    while n + pow(2, j) < len_ls:
        all.append(ls[n: n + pow(2, j)])
        n = n + pow(2, j)
        j += 1

    # 保存头节点，从ls里面吧头节点删掉
    begin = ls.pop(0)
    for i in all:
        while len(i):
            if i[0].val:
                left = ls.pop(0)
                if left.val:
                    i[0].left = left
                right = ls.pop(0)
                if right.val:
                    i[0].right = right
            else:
                ls.pop(0)
                ls.pop(0)
            i.pop(0)
    return begin


def LDR(tree: TreeNode) -> list:
    if not tree:
        return []
    LDR(tree.left)
    res.append(tree.val)
    LDR(tree.right)
    return res


if __name__ == '__main__':
    ls = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    data = convert_list_to_tree(ls)
    print(data)
