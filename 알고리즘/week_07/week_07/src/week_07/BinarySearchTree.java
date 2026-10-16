package week_07;

public class BinarySearchTree {
	private TreeNode rootNode;

	public TreeNode BSTsearch(String K) {
		// 코드 작성
		TreeNode p = rootNode;

		while (p != null) {
			int result = K.compareTo(p.key);

			if (result == 0)
				return p;
			else if (result < 0)
				p = p.Lchild;
			else
				p = p.Rchild;
		}

		return null;
	}

	public void BSTinsert(String K) {
		// 코드 작성
		TreeNode newNode = new TreeNode();
		newNode.key = K;
		newNode.Lchild = null;
		newNode.Rchild = null;

		if (rootNode == null) {
			rootNode = newNode;
			return;
		}

		TreeNode p = rootNode;
		TreeNode parent = null;

		while (p != null) {
			parent = p;

			int result = K.compareTo(p.key);

			if (result == 0)
				return;
			else if (result < 0)
				p = p.Lchild;
			else
				p = p.Rchild;
		}

		if (K.compareTo(parent.key) < 0)
			parent.Lchild = newNode;
		else
			parent.Rchild = newNode;
	}

	private TreeNode maxNode(TreeNode root) {
		// 코드 작성
		if (root == null)
			return null;

		while (root.Rchild != null) {
			root = root.Rchild;
		}

		return root;
	}

	private TreeNode delete(TreeNode root, String K) {
		// 코드 작성
		if (root == null)
			return null;

		int result = K.compareTo(root.key);

		if (result < 0) {
			root.Lchild = delete(root.Lchild, K);
		} else if (result > 0) {
			root.Rchild = delete(root.Rchild, K);
		} else {
			// 자식이 없는 경우 또는 오른쪽 자식만 있는 경우
			if (root.Lchild == null)
				return root.Rchild;

			// 왼쪽 자식만 있는 경우
			if (root.Rchild == null)
				return root.Lchild;

			// 자식이 두 개 있는 경우
			TreeNode temp = maxNode(root.Lchild);
			root.key = temp.key;
			root.Lchild = delete(root.Lchild, temp.key);
		}

		return root;
	}

	public void BSTdelete(String K) {
		rootNode = delete(rootNode, K);
	}

	public boolean BSTsplit(String x, BinarySearchTree SmallTree, BinarySearchTree LargeTree) {
		// 코드 작성
		// 기존 분할 트리 초기화
		SmallTree.rootNode = null;
		LargeTree.rootNode = null;

		// 원본 트리가 비어 있는 경우
		if (rootNode == null)
			return false;

		java.util.Stack<TreeNode> stack = new java.util.Stack<>();
		stack.push(rootNode);

		boolean found = false;

		while (!stack.isEmpty()) {
			TreeNode p = stack.pop();

			int result = p.key.compareTo(x);

			if (result < 0) {
				// x보다 작은 키
				SmallTree.BSTinsert(p.key);
			} else if (result > 0) {
				// x보다 큰 키
				LargeTree.BSTinsert(p.key);
			} else {
				// x와 같은 키
				found = true;
			}

			// 오른쪽 자식 확인
			if (p.Rchild != null)
				stack.push(p.Rchild);

			// 왼쪽 자식 확인
			if (p.Lchild != null)
				stack.push(p.Lchild);
		}

		return found;
	}

	private void printNode(TreeNode n) {
		if (n != null) {
			System.out.print("(");
			printNode(n.Lchild);
			System.out.print(" " + n.key + " ");
			printNode(n.Rchild);
			System.out.print(")");
		}
	}

	public void print() {
		printNode(rootNode);
		System.out.println();
	}
}
