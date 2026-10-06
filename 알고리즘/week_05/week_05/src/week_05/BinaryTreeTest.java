package week_05;

public class BinaryTreeTest {
	public static void main(String args[]) {
		BinaryTree btree;
		BinaryTree ltree;
		BinaryTree rtree;
		BinaryTree current;
		rtree = new BinaryTree(new BinaryTree(), "H", new BinaryTree());
		btree = new BinaryTree(new BinaryTree(), "G", rtree);
		ltree = btree;
		btree = new BinaryTree(ltree, "E", new BinaryTree());
		ltree = new BinaryTree(new BinaryTree(), "D", new BinaryTree());
		rtree = btree;
		btree = new BinaryTree(ltree, "B", rtree);
		ltree = new BinaryTree(new BinaryTree(), "F", new BinaryTree());
		current = new BinaryTree(ltree, "C", new BinaryTree());
		ltree = btree;
		rtree = current;
		btree = new BinaryTree(ltree, "A", rtree);
		System.out.println(btree.rootData());
		System.out.println(btree.leftSubTree().rootData());
		System.out.println(btree.rightSubTree().rootData());
		System.out.println(btree.leftSubTree().leftSubTree().rootData());
		System.out.println(btree.rightSubTree().leftSubTree().rootData());
		btree.inorder();
		System.out.println();
		btree.preorder();
		System.out.println();
		btree.postorder();
		System.out.println();
		btree.levelorder();
		System.out.println();
		current = btree.copy();
		current.inorder();
		System.out.println();
		if (btree.equals(current))
			System.out.println("They are the same trees");
		else
			System.out.println("They are different trees");
		if (btree.equals(ltree))
			System.out.println("They are the same trees");
		else
			System.out.println("They are different trees");
	}
}
