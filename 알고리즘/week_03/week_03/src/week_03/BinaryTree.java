package week_03;

public class BinaryTree {
	BTNode root;

	public BinaryTree() {
		// 코드 작성
		root = null;
		
	}

	public BinaryTree(BinaryTree ltree, String data, BinaryTree rtree) {
		// 코드 작성
		root = new BTNode(ltree.root,data,rtree.root);
	}

	public boolean isEmpty() {
		// 코드 작성
		return root == null;
	}

	public BinaryTree leftSubTree() {
		// 코드 작성
		BinaryTree tmp = new BinaryTree();
		if(root != null) {
			tmp.root = root.Lchild;
		}
		return tmp;
	}

	public BinaryTree rightSubTree() {
		// 코드 작성
		BinaryTree tmp = new BinaryTree();
		if(root != null) {
			tmp.root = root.Rchild;
		}
		return tmp;
	}

	public String rootData() {
		// 코드 작성
		if(root == null) {
			System.out.println("빈루트");
			return null;
		}
		return root.data;
	}

	public int calculate() {
		// 코드 작성
		return theCalculate(root);
	}

	private int theCalculate(BTNode t) {
		// 코드 작성
		if (t.Lchild == null && t.Rchild == null) {
            return Integer.parseInt(t.data);
        }
		int left = theCalculate(t.Lchild);
        int right = theCalculate(t.Rchild);

        switch (t.data) {
            case "+":
                return left + right;

            case "-":
                return left - right;

            case "*":
                return left * right;

            case "/":
                return left / right;

            default:
                return 0;
        }
	}

	public int height() {
		// 코드 작성
		return theHeight(root);
	}

	private int theHeight(BTNode t) {
		// 코드 작성
		if(t == null) {
			return -1;
		}
		int leftHeight = theHeight(t.Lchild);
		int rightHeight = theHeight(t.Rchild);
		
		return 1 + Math.max(leftHeight, rightHeight);
	}

	public void print0() {
		// 코드 작성
		print0(root);
        System.out.println();
	}

	private void print0(BTNode t) {
		// 코드 작성
		if(t==null)return;
		
		if (t.Lchild == null && t.Rchild == null) {
            System.out.print(t.data);
            return;
        }
		
		System.out.print("(");

        print0(t.Lchild);

        System.out.print(t.data);

        print0(t.Rchild);

        System.out.print(")");
	}	
}
