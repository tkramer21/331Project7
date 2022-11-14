# Adelson-Velsky and Landis Trees--> Self Balancing BSTs

**Due: Wednesday, November 16th 10:00pm EST**

_This is not a team project. Do not copy someone else’s work._

## Assignment Overview

[AVL trees](https://en.wikipedia.org/wiki/AVL_tree) are a self-balancing [binary search tree (BST)](https://en.wikipedia.org/wiki/Binary_search_tree) optimized to maintain logarithmic-time operations regardless of the order in which data is inserted and deleted. First introduced by Soviet computer scientists Georgy Adelson-Velsky and Evgenii Landis in their 1962 paper "[An algorithm for the organization of information](https://zhjwpku.com/assets/pdf/AED2-10-avl-paper.pdf)," AVL trees have stood the test of time and remain a popular choice when a space-efficient data structure supporting fast insertion/search/deletion is necessary.

![](img/avl.gif)

To motivate AVL trees, it is worth considering a common problem that arises in traditional BSTs. BSTs are designed to perform logarithmic-time insertion/search/deletion, but may operate at linear-time if data is inserted or deleted according to certain patterns which cause the BST to become _unbalanced_. For example, when data is inserted into a traditional BST in sorted (or reverse-sorted) order, the BST will grow leaves in a single direction and effectively turn into a linked list.

![](img/balance.png)

If our dataset is small, this may not be a problem—but when we're working with thousands or millions of records in a database, the difference between logarithmic and linear is astounding!

![](img/bigogrowth.png)

AVL trees improve upon traditional BSTs by _self-balancing_ in order to guarantee logarithmic-time operations. In this project, you will be implementing an AVL tree from scratch in Python. For more information on BSTs and AVL Trees, check out D2L Week7-8 content.

## Assignment Notes

1. In this project, you'll be using Python `Generator` objects to traverse a tree in a space-efficient manner. Unlike a traversal returned in the form `List[Node]` using _O(n)_ space, a traversal returning a generator will use _O(1)_ space by _yielding_ each `Node` in a sequential, on-demand manner. See [this link](https://realpython.com/introduction-to-python-generators/) for a nice introduction to `Generator`s in Python! 
You can also look back at the Week 7-8  on D2L for Yield.
2. One of the most common errors in this project is forgetting or incorrectly updating the height and rebalancing within functions that change the tree structure (insert and remove). Read the notes we put under the function description in the specs carefully and think about how you can use recursion/the call stack to help you rebalance the tree. What is the call stack's relationship to the node which you removed/inserted?....

3. AVL Trees are more complicated structures than what you have worked with before but if you boil each function down to the different cases within them, then it begins to look a lot simpler. Try to decompose each function into what checks/cases you need to look for before an operation. Checks like is the node I'm removing/inserting the origin? Is there a right node before I make a call on node.right? Am I updating the correct pointers?

4. The debugger is your friend! Do not be scared to use it, it is worth the extra time to learn its functionality if you haven't yet. Use it to determine if what you think your code is doing, is actually what it's doing! It's the most helpful tool when trying to figure out why your more complex functions aren't working.

5. We have provided visualization and printing functions for when you just want to get a birds eye view of your tree and don't want to have to click through several levels of objects in the debugger. Using the visualization functions is as simple as calling `tree.visualize()` on an object of type AVLTree. We are, of course, human, and cannot guarantee these visualizations are 100% bug free; if you encounter issues, let us know.

6. Using global variables (with the nonlocal keyword) will result in a 20 point flat-rate deduction.

7. Changing function signatures will result in a 2 point deduction for each violation, up to a maximum of 20 points.

8. If you run the solution.py file after implementing all AVLTree functions, you will be greeted by a performance comparison between the two trees!


 
## Assignment Specifications

#### class Node:

Implements a tree node used in the AVLTree classes.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **value: T:** Value held by the `Node`. Note that this may be any type, such as a `str`, `int`, `float`, `dict`, or a more complex object.
  - **parent: Node:** Reference to this `Node`'s parent `Node` (may be `None`).
  - **left: Node:** Reference to this `Node`'s left child `Node` (may be `None`).
  - **right: Node:** Reference to this `Node`'s right child `Node` (may be `None`).
  - **height: int:** Number of levels of `Node`s below (the height of a leaf `Node` is 0).
- **\_\_init\_\_(self, value: T, parent: Node = None, left: Node = None, right: Node = None) -> None**
  - Constructs an AVL Tree node.
  - **value: T:** Value held by the `Node`.
  - **parent: Node:** Reference to this `Node`'s parent `Node` (may be `None`).
  - **left: Node:** Reference to this `Node`'s left child `Node` (may be `None`).
  - **right: Node:** Reference to this `Node`'s right child `Node` (may be `None`).
  - **Returns:** `None`.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the `Node` as a string in the form `<value_held_by_node>`. Thus, `<7>` indicates a `Node` object holding an `int` value of 7, whereas `<None>` indicates a `Node` object holding a value of `None`.
  - Note that Python will automatically invoke this function when using printing a `Node` to the console, and PyCharm will automatically invoke this function when displaying a `Node` in the debugger.
  - Call this with `str(node)` (rather than `node.__str__()`).
  - **Returns:** `str`.  
  
#### class AVLTree:

Implements a self-balancing BSTree for faster operation.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **origin: Node:** Root node of the entire `AVLTree` (may be `None`). This naming convention helps us disambiguate between when we are referring to the root of the entire `AVLTree` and the root of a subtree within the `AVLTree`. In fact, any given `Node` object within an `AVLTree` can be thought of as being the root of the subtree of all `Node`s below—and `origin` is the uppermost such root in our tree.
  - **size: int:** Number of nodes in the `AVLTree`.
- **\_\_init\_\_(self) -> None**
  - Construct an empty `AVLTree`. Initialize the `origin` to `None` and set the size to zero.
  - **Returns:** `None`.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Returns a pretty printed string representation of the binary tree. Each node will be of the form `{value},h={height},⬆{parent.value}`
  - Note that Python will automatically invoke this function when printing a `Node` to the console, and PyCharm will automatically invoke this function when displaying a `Node` in the debugger.
  - Call this with `str(node)` (rather than `node.__str__()`).
  - **Returns:** `str`.

- **visualize(self, filename="avl_tree_visualization.svg") -> str**
  - Generates an svg image file of the binary tree.
  - filename: str: The filename for the generated svg file. Should end with .svg. Defaults to avl_tree_visualization.svg
  - **Returns:** The svg string.

- **height(self, root: Node) -> int**
  - Returns height of a subtree in the AVL tree, properly handling the case of `root = None`. Recall that the height of an empty subtree is -1.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree being measured.
  - **Returns:** Height of the subtree at `root`, i.e., the number of levels of `Node`s below this `Node`. The height of a leaf `Node` is 0, and the height of a `None`-type is -1.

- **left_rotate(self, root: Node) -> Node**
  - Perform a left rotation on the subtree rooted at `root`. Return root of new subtree after rotation.
  - This method is already implemented for you.
  - _Time / Space: O(1) / O(1)_.
  - **root: Node:** The root `Node` of the subtree being rotated.
  - **Returns:** Root of new subtree after rotation.
 
- **remove(self, root: Node, val: T) -> Node**
  - This method is already implemented for you.
  - Removes the node with value `val` from the subtree rooted at `root`, and returns the root of the balanced subtree following removal.
  - If `val` does not exist in the AVL tree, do nothing.
  - Updates `size` and `origin` attributes of `AVLTree` and correctly update parent/child pointers of `Node` objects as necessary.
  - Updates the `height` attribute and call `rebalance` on all `Node` objects affected by the removal (ancestor nodes directly above on path to origin).
  - Note that that there are [three distinct cases of BST removal to consider](https://en.wikipedia.org/wiki/Binary_search_tree#Deletion).
  - Implemented recursively.
  - If the node being removed has two children, swaps the value of this node with its **predecessor** and recursively removes this predecessor node (which contains the value to be removed after swapping and is guaranteed to be a leaf).
    - Although one technically _could_ swap values with the successor node in a two-child removal, we choose to swap with the predecessor.
  - _Time / Space: O(log n) / O(1)_.
  - **root: Node:** The root `Node` of the subtree from which to delete `val`.
  - **val: T:** The value to be deleted from the subtree rooted at `root`.
  - **Returns:** Root of new subtree after removal and rebalancing (could be the original root).

_IMPLEMENT the following functions_
- **right_rotate(self, root: Node) -> Node**
  - Perform a right rotation on the subtree rooted at `root`. Return root of new subtree after rotation.
  - This should be nearly identical to `left_rotate`, with only a few lines differing. Team 331 agreed that giving one rotation helps ease the burden of this project, but writing the other rotation will be a good learning experience!
  - *Time* : O(1)
  - **root: Node:** The root `Node` of the subtree being rotated.
  - **Returns:** Root of new subtree after rotation.
- **balance_factor(self, root: Node) -> int**
  - Compute the balance factor of the subtree rooted at `root`.
  - Recall that the balance factor is defined to be $h_L$ - $h_R$ where $h_L$ is the height of the left subtree beneath this `Node` and $h_R$ is the height of the right subtree beneath this `Node`.
  - Note that in a properly-balanced AVL tree, the balance factor of all nodes in the tree will be in the set {-1, 0, +1}, as rebalancing will be triggered when a node's balance factor becomes -2 or +2.
  - The balance factor of an empty subtree (`None`-type `root`) is 0.
  - To stay within time complexity, keep the `height` attribute of each `Node` object updated on all insertions/deletions/rebalances, then use $h_L$ = `left.height` and $h_R$ = `right.height`.
  - *Time: O(1)*
  - **root: Node:** The root `Node` of the subtree on which to compute the balance factor.
  - **Returns:** `int` representing the balance factor of `root`.
- **rebalance(self, root: Node) -> Node**
  - Rebalance the subtree rooted at `root` (if necessary) and return the new root of the resulting subtree.
  - Recall that rebalancing is only necessary at this `root` if the balance factor `b` of this `root` satisfies `b >= 2 or b <= -2`.
  - Recall that there are [four types of imbalances possible in an AVL tree](https://en.wikipedia.org/wiki/AVL_tree#Rebalancing), and that each requires a different sequence of rotation(s) to be called.
  - _Time O(1)_.
  - **root: Node:** The root `Node` of the subtree to be rebalanced.
  - **Returns:** Root of new subtree after rebalancing (could be the original root).
- **insert(self, root: Node, val: T) -> Node**
  - Insert a node with `val` into the subtree rooted at `root`, returning the root node of the balanced subtree after insertion.
  - If `val` already exists in the AVL tree, do nothing.
  - Should update `size` and `origin` attributes of `AVLTree` if necessary and correctly set parent/child pointers when inserting a new `Node`
  - Should update the `height` attribute and call `rebalance` on all `Node` objects affected by the insertion (ancestor nodes directly above on path to origin).
  - Easiest to implement recursively.
  - **_Time / Auxiliary Space: O(log n) / O(1)_.**
  - **root: Node:** The root `Node` of the subtree in which to insert `val`.
  - **val: T:** The value to be inserted in the subtree rooted at `root`.
  - **Returns:** Root of new subtree after insertion and rebalancing (could be the original root).
- **min(self, root: Node) -> Node**
  - Find and return the `Node` with the smallest value in the subtree rooted at `root`.
  - Easiest to implement recursively.
  - _Time: O(log n)_.
  - **root: Node:** The root `Node` of the subtree in which to search for a minimum.
  - **Returns:** `Node` object containing the smallest value in the subtree rooted at `root`.
- **max(self, root: Node) -> Node**
  - Find and return the `Node` with the largest value in the subtree rooted at `root`.
  - Easiest to implement recursively.
  - _Time: O(log n)_.
  - **root: Node:** The root `Node` of the subtree in which to search for a maximum.
  - **Returns:** `Node` object containing the largest value in the subtree rooted at `root`.
- **search(self, root: Node, val: T) -> Node**
  - Find and return the `Node` with the value `val` in the subtree rooted at `root`.
  - If `val` does not exist in the subtree rooted at `root`, return the `Node` below which `val` would be inserted as a child. For example, on a balanced 1-2-3 tree (with 2 on top and 1, 3 as children), `search(node_2, 0)` would return `node_1` since the value of 0 would be inserted as a left child of `node_1`.
  - Easiest to implement recursively.
  - _Time: O(log n)_.
  - **root: Node:** The root `Node` of the subtree in which to search for `val`.
  - **val: T:** The value being searched in the subtree rooted at `root`.
  - **Returns:** `Node` object containing `val` if it exists, else the `Node` object below which `val` would be inserted as a child.
  
- **inorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform an inorder (left, current, right) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - **To pass the test case for this function, you must also make the AVLTree class iterable such that doing `for node in avltree` iterates over the inorder traversal of the tree**
  - *Time : O(n) .*
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
  
- **\_\_iter\_\_(self) -> Generator[Node, None, None]**
  - Implementing this "dunder" method allows you to use an AVL tree class object anywhere you can use an iterable, e.g., inside of a `for node in tree` expression. We want the iteration to use the inorder traversal of the tree so this should be implemented such that it returns the inorder traversal. 
  - **This function should only be one line, calling another function you have implemented.**
  - **Returns:** A generator that iterates over the inorder traversal of the tree
  
- **preorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a preorder (current, left, right) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - - *Time : O(n) .*
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
  
- **postorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a postorder (left, right, current) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - - *Time : O(n) .*
    - Although we will traverse the entire tree and hence incur O(n) time, our use of a generator will keep us at constant space complexity since elements are yielded one at a time! This is a key advantage of returning a generator instead of a list.
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.
- **levelorder(self, root: Node) -> Generator[Node, None, None]**
  - Perform a level-order (breadth-first) traversal of the subtree rooted at `root` using a [Python generator](https://realpython.com/introduction-to-python-generators/).
  - Use the builtin `queue.SimpleQueue` class to maintain your queue of children throughout the course of the traversal—[see the official documentation here.](https://docs.python.org/3/library/queue.html#queue.SimpleQueue) It is **highly** recommended that you use the `SimpleQueue` instead of implementing your own.
  - Use `yield` to immediately generate an element in your function, and `yield from` to generate an element from a recursive function call.
  - Do not yield (generate) `None`-types.
  - - *Time : O(n) .*
    - We will traverse the entire tree and incur O(n) time. In addition, the queue we must use for an inorder traversal will grow to size n/2 = O(n) just before beginning the final level of leaf nodes in the case of a [perfect binary tree.](https://www.programiz.com/dsa/perfect-binary-tree)
  - **root: Node:** The root `Node` of the subtree currently being traversed.
  - **Returns:** `Generator` object which yields `Node` objects only (no `None`-type yields). Once all nodes of the tree have been yielded, a `StopIteration` exception is raised.

## Application: Valid AVL Tree ##
"_There are more trees than our project needs._" This is what your boss told you in the meeting of making a tree-like data-structure for your company's next big project. As the intern of this team, you want to impress your boss by identifying balanced binary search trees, or AVL trees, in the forest of tree-like structures. You know from CSE 331 that an AVL tree could improve the running time for searching, inserting, and deleting compared to an ordinary tree. To secure your future job, you must complete this task as soon as possible.  
To do this application problem, you need to implement one function, `is_avl_tree`.
- **is_avl_tree(node: Node) -> boolean**
  - Given a of `Binary Tree`, determine whether given tree is valid or invalid AVL tree by the properties of
AVL tree
  - **Only left, right, and val attributes of Node and origin of AVLTree are allowed to use**
  - You may not use other Node's attributes or previously implemented AVL tree function in this function. Otherwise, **it will result in a zero for both automatic and manual score**
  **- _Time / Auxiliary Space: O(n) / O(1)_.**
  - Auxiliary space is space using in this function only
  - **tree: AVLTree** Given tree to verify
  - **Return** `boolean` indicate whether given tree is valid AVL tree or not
  - To be valid AVL tree, given tree need to satisfy binary tree properties, left subtree < root < right subtree, and 
AVL tree property, balance of tree
  - **Only attributes allowed to use in this application problem are left, right, and val of Node and origin of AVLTree.** Other functions and attributes are not allow to use.
  - _Note: the is_avl_tree function will not depend on any of the code that you were required to implement for the AVLTree class.
The tree is made using only value, left and right. This means that the parent, height, and depth are not updated.
If you are stuck on the AVLTree code, you can still pass this test case as it is independent._  
  - _Note2: If you want to use infinite or negative infinite value, let use float('inf') and -float('inf'), respectively._

### Examples:  
Example 1.  
![](img/app1.png)

AVLTree: The AVLTree provided above
Return: True, this tree satisfies all AVL tree properties  

Example 2.  
![](img/app2.png)

AVLTree: The AVLTree provided above
Return: False, this is binary search tree, but it's imbalance at Node(20) and Node(10)  

Example 3.  
![](img/app3.png)

AVLTree: The AVLTree provided above
Return: False, this tree is not binary search tree, 12 in the left subtree of 10 but 12 >= 10. Then, it's not AVL tree.
  

## **Submission**


#### **Deliverables**
In every project you will be given a file named as "**solution.py**". Your will work on this file to write your Python code.
We recommend that you **download your "solution.py" and "tests.py" to your local drive**, and work on your project using PyCharm so you can easily debug your code.

Below are the simple steps to work on any project locally in your personal computer in this class:

**APPROACH 1: USING D2L TO DOWNLOAD PROJECT'S STARTER PACKAGE:**
1. Make sure you installed PyCharm
2. You can download the starter package from D2L under Projects content. Watch the short tutorial video on how to download the starter package from D2L and open it up in PyCharm.
3. Work on your project as long as you want then upload your solution.py , (watch the short tutorial video on D2L for uploading your solution.py), and upload your solution.py to Codio.
4. Click Submit button on Guide when you are done!
![](img/Submit.png)

**APPROACH 2: USING CODIO TO DOWNLOAD solution.py and tests.py**
1. On your own computer make sure to create a local folder in your local drive, name it something like **ProjectXX**, replace xx with the actual project number, in this case your folder name would be **Project03**.
2. **Download** solution.py from Codio by simply right mouse clicking on the file tree, see image below
![](img/Codio_FileTree.png)
3. **Download** tests.py from Codio by simply right mouse clicking on the file tree as shown above.
4. Work locally using PyCharm as long as you need. 
5. When finished with your solution.py file, upload your file to Codio by right mouse clicking on the Project Directory on file tree.You should rename or remove the solution.py file that is currently existing in Codio before you upload your completed version. 
6. Go To Guide and click Submit button
![](img/Codio_Upload.png)


**It does not matter which approach you choose to work on your project, just be sure to upload your solution, “solution.py”, to Codio by and click on the Submit button by its deadline.**
Working locally is recommended so you can learn debugging. You can complete your entire solution.py using Codio editor, debugging may not as intuitive as PyCharm IDE. For this reason we recommend that you work locally as long as you need, then upload your code to Codio.


**Grading**

* **Auto Graded Tests (70 points)** see below for the point distribution for the auto graded tests:

      1.  right_rotate:     5 points
      2.  balance_factor:   5 points
      3.  rebalance:        5 points
      4.  insert:           10 points
      5.  min:              5 points
      6.  max:              5 points
      7.  search:           5 points
      8.  inorder/__iter__: 5 points
      9.  preorder:         5 points
      10. postorder:       5 points
      11. levelorder:      5 points
      12. is_avl_tree_basic( application problem ):  5 points
      13. is_avl_tree( application problem ):        5 points

* **Manual (30 points)**
- See the time complexity requirement for each function listed below. 
- Auxiliary Space complexity requirement is only enforced for insert, and the application problem. Since we already completed the remove for you, no run time or space complexity check on that function.
  * Loss of 1 point per missing docstring (max 5 point loss)
  * Loss of 2 points per changed function signature (max 20 point loss)
  * Loss of complexity and loss of testcase points for the required functions in this project. You may not use any additional data structures such as dictionaries, and sets!”
  * Loss all points for application problem if use other AVL functions and attributes other than origin, left, right, and val
  Below is the list of manual points for the functions
      1.  right_rotate:    \_\_/1 points
      2.  balance_factor:  \_\_/1 points
      3.  rebalance:        \_\_/4 points
      4.  insert:           \_\_/4 points (run time and space)
      5.  min:              \_\_/2 points
      6.  max:              \_\_/2 points
      7.  search:           \_\_/2 points
      8.  inorder/__iter__: \_\_/2 points
      9.  preorder:         \_\_/2 points
      10. postorder:       \_\_/2 points
      11. levelorder:      \_\_/2 points
      12. is_avl_tree_(application problem ):  \_\_/4 points (run time and space)
      13. Feedback and citation. See text box below to complete.\_\_/2  points


* **Important reminder**
Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.


    * **DOCSTRING** is not provided for this project. Please use Project 1 as a template for your DOCSTRING . 
    To learn more on what is a DOCSTRING visit the following website: [What is Docstring?](https://peps.python.org/pep-0257/)
      * One point per function that misses DOCSTRING.
      * Up to 5 points of deductions

<input type="checkbox"> <b>STEP 1 :Rename the old solution file by clicking Rename button below. This button renames your file to **solution_old.py** </b>
{Rename}(mv solution.py solution_old.py)
<input type="checkbox"> <b>STEP 2 : Refresh your file tree by clicking on the refresh button under project name or refresh your browser. </b>

<input type="checkbox"> <b>STEP 3 : Upload your **solution.py** from your computer to Codio File Tree on the left. Refresh your file tree or browser to see if it actually updated the solution.py </b>


<input type="checkbox"> <b>STEP 4:Submit your code, by clicking the Submit button, you can submit as many times as you like, no limit on submission. 

Run button is removed. Run button was tied to tests.py in your file tree and in case of an update on tests.py , students who already started the work, would not see the update using the Run button.
Submit button is tied to tests.py in our secure folder, and it always gets the updated version of the tests.py. In case of any tests.py, students will always get the latest version to test their code through the submit button. In case of an update, the updated tests.py will be given through D2L or on Piazza so students can locally test it using their IDE. :</b>
{SUBMIT!|assessment}(test-3379255259)
Please note that there will be manual grading after you submit your work. Clicking Submit only runs the Auto-grader for the test cases. Manual Grading is 30 points in this project. (28 pts for Run Time and Space complexity, +2 points for filling out the feedback and the citation text box)


<input type="checkbox"> <b>STEP 5: Please make sure to scroll down on Guide Editor page, which is this page, click at the mark complete button, see below for the image of the button. </b>
![](img/markcomplete.png)

{Check It!|assessment}(grade-book-3266829715)
{Submit Answer!|assessment}(free-text-3024451938)










## Appendix

#### Authors

Project authored by Bank Premsri. 
Adapted from work by Andrew McDonald, Lukas Richters, and Joseph Pallipadan.

#### Memes

![](img/tree.jpg)

![](img/thanos.jpg)

![](img/bestworst.png)
