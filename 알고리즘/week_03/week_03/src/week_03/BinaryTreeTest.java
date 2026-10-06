package week_03;

public class BinaryTreeTest {
	public static void main(String args[]) {
		BinaryTree btree;
		BinaryTree ltree;
		BinaryTree rtree;
		BinaryTree current;
		rtree = new BinaryTree(new BinaryTree(), "1", new BinaryTree());
		ltree = new BinaryTree(new BinaryTree(), "2", new BinaryTree());
		btree = new BinaryTree(ltree, "+", rtree);
		ltree = btree;
		rtree = new BinaryTree(new BinaryTree(), "3", new BinaryTree());
		btree = new BinaryTree(ltree, "*", rtree);
		System.out.println("계산 결과 : " + btree.calculate());
		System.out.print("수식 출력 : ");
		btree.print0();
		System.out.println("트리의 높이 : " + btree.height());
	}
}
