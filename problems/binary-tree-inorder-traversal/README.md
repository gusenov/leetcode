# [Depth-first search](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search) ([поиск в глубину](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%85%D0%BE%D0%B4_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%B0#%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83))

## [In-order, LNR](https://en.wikipedia.org/wiki/Tree_traversal#In-order,_LNR) ([центрированный обход (LNR)](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%85%D0%BE%D0%B4_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%B0#%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BE%D0%B1%D1%85%D0%BE%D0%B4_(LNR)))

0. Проверяем, не является ли текущий узел пустым или null.
1. Recursively traverse the current node's left subtree. (Обходим левое поддерево рекурсивно, вызвав функцию центрированного обхода.)
2. Visit the current node (in the figure: position green). (Показываем поле данных корня (или текущего узла).)
3. Recursively traverse the current node's right subtree. (Обходим правое поддерево рекурсивно, вызвав функцию центрированного обхода.)

In a binary search tree ordered such that in each node the key is greater than all keys in its left subtree and less than all keys in its right subtree, in-order traversal retrieves the keys in ascending sorted order.
(В двоичном дереве поиска центрированный обход извлекает данные в отсортированном порядке.)

![](Sorted_binary_tree_ALL_RGB.svg)

Depth-first traversal (dotted path) of a binary tree:

- Pre-order (node visited at position red 🔴):
   - F, B, A, D, C, E, G, I, H;
- In-order (node visited at position green 🟢):
   - A, B, C, D, E, F, G, H, I;
- Post-order (node visited at position blue 🔵):
   - A, C, E, D, B, H, I, G, F.

![](Sorted_binary_tree_inorder.svg)

Центрированный обход: A, B, C, D, E, F, G, H, I.
