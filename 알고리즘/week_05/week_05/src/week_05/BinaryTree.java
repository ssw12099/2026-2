package week_05;

public class BinaryTree {
	BTNode root;

	public BinaryTree() {
		root = null;
	}

	public BinaryTree(BinaryTree ltree, String data, BinaryTree rtree) {
		root = new BTNode(ltree.root, data, rtree.root);
	}

	public boolean isEmpty() {
		return root == null;
	}

	public BinaryTree leftSubTree() {
		BinaryTree ltree = new BinaryTree();
		ltree.root = root.Lchild;
		return ltree;
	}

	public BinaryTree rightSubTree() {
		BinaryTree rtree = new BinaryTree();
		rtree.root = root.Rchild;
		return rtree;
	}

	public String rootData() {
		return root.data;
	}

	public void inorder() {
		System.out.println();
		System.out.println("Inorder");
		theInorder(root);
		System.out.println();
		System.out.println("InorderIter");
		inorderIter1();
	}

	public void preorder() {
		System.out.println("preorder");
		System.out.println();
		thePreorder(root);
		System.out.println();
		System.out.println("preorderIter");
		preorderIter();
	}

	public void postorder() {
		thePostorder(root);
	}

	private void theInorder(BTNode t) {
		// 코드 작성
		 if (t != null) {
	            theInorder(t.Lchild);

	            System.out.print(t.data);

	            theInorder(t.Rchild);
	        }
	}

	private void thePreorder(BTNode t) {
		// 코드 작성
		 if (t != null) {
	            System.out.print(t.data);

	            thePreorder(t.Lchild);

	            thePreorder(t.Rchild);
	        }
	}

	private void thePostorder(BTNode t) {
		// 코드 작성
		if (t != null) {
            thePostorder(t.Lchild);

            thePostorder(t.Rchild);

            System.out.print(t.data);
        }
	}

	private void inorderIter1() {
		// 코드 작성
		Stack stack = new Stack();

        BTNode current = root;

        while (current != null || !stack.empty()) {

            // 가장 왼쪽 노드까지 이동
            while (current != null) {
                stack.push(current);
                current = current.Lchild;
            }

            // Stack에서 하나 꺼냄
            current = (BTNode) stack.pop();

            System.out.print(current.data);

            // 오른쪽 서브트리 이동
            current = current.Rchild;
        }
	}

	private void preorderIter() {
		// 코드 작성
		if (root == null)
            return;

        Stack stack = new Stack();

        stack.push(root);

        while (!stack.empty()) {

            BTNode current = (BTNode) stack.pop();

            System.out.print(current.data);

            // Stack은 LIFO이므로
            // 오른쪽 먼저 왼쪽 나중
            if (current.Rchild != null)
                stack.push(current.Rchild);

            if (current.Lchild != null)
                stack.push(current.Lchild);
        }
	}

	public void levelorder() {
		// 코드 작성
		if (root == null)
            return;

        Queue queue = new Queue();

        queue.enqueue(root);

        while (!queue.isEmpty()) {

            BTNode current = (BTNode) queue.dequeue();

            System.out.print(current.data);

            if (current.Lchild != null)
                queue.enqueue(current.Lchild);

            if (current.Rchild != null)
                queue.enqueue(current.Rchild);
        }
	}

	public BinaryTree copy() {
		// 코드 작성
		BinaryTree newTree = new BinaryTree();

        newTree.root = theCopy(root);

        return newTree;
	}

	private BTNode theCopy(BTNode t) {
		// 코드 작성
		if (t == null)
            return null;

        BTNode newNode =
                new BTNode(
                        theCopy(t.Lchild),
                        t.data,
                        theCopy(t.Rchild)
                );

        return newNode;
	}

	public boolean equals(BinaryTree tr) {
		return theEqual(this.root, tr.root);
	}

	private boolean theEqual(BTNode s, BTNode t) {
		// 둘다 널
		if (s == null && t == null)
            return true;

        // 둘 중 하나만 널
        if (s == null || t == null)
            return false;

        // 데이터가 다르면 다른 트리
        if (!s.data.equals(t.data))
            return false;

        // 왼쪽 오른쪽 모두 비교
        return theEqual(s.Lchild, t.Lchild)
                && theEqual(s.Rchild, t.Rchild);
	}
}
