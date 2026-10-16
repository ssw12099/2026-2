package week_07;

public class BSTTest {
	public static void main(String[] args) {
		BinarySearchTree t = new BinarySearchTree();
		t.BSTinsert("S");
		t.BSTinsert("J");
		t.BSTinsert("B");
		t.BSTinsert("D");
		t.BSTinsert("U");
		t.BSTinsert("M");
		t.BSTinsert("R");
		t.BSTinsert("Q");
		t.BSTinsert("A");
		t.BSTinsert("G");
		t.BSTinsert("E");
		System.out.println("===== 초기 이진 탐색 트리 =====");
		t.print();
		System.out.println("===== R 검색 =====");
		TreeNode n = t.BSTsearch("R");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("===== R 삭제 후 검색 =====");
		t.BSTdelete("R");
		n = t.BSTsearch("R");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("R 삭제 후 트리");
		t.print();
		System.out.println("===== E 검색 =====");
		n = t.BSTsearch("E");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("===== E 삭제 후 검색 =====");
		t.BSTdelete("E");
		n = t.BSTsearch("E");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("E 삭제 후 트리");
		t.print();
		System.out.println("===== J 검색 및 삭제 =====");
		n = t.BSTsearch("J");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		t.BSTdelete("J");
		System.out.println("J 삭제 후 검색");
		n = t.BSTsearch("J");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("J 삭제 후 트리");
		t.print();
		System.out.println("===== S 검색 및 삭제 =====");
		n = t.BSTsearch("S");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		t.BSTdelete("S");
		System.out.println("S 삭제 후 검색");
		n = t.BSTsearch("S");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("S 삭제 후 트리");
		t.print();
		System.out.println("===== B 검색 및 삭제 =====");
		n = t.BSTsearch("B");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		t.BSTdelete("B");
		System.out.println("B 삭제 후 검색");
		n = t.BSTsearch("B");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("B 삭제 후 트리");
		t.print();
		System.out.println("===== 존재하지 않는 C 검색 =====");
		n = t.BSTsearch("C");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("===== 새로운 이진 탐색 트리 t1 생성 =====");
		BinarySearchTree t1 = new BinarySearchTree();
		t1.BSTinsert("S");
		t1.BSTinsert("J");
		t1.BSTinsert("B");
		t1.BSTinsert("D");
		t1.BSTinsert("U");
		t1.BSTinsert("M");
		t1.BSTinsert("R");
		t1.BSTinsert("Q");
		t1.BSTinsert("A");
		t1.BSTinsert("G");
		t1.BSTinsert("E");
		System.out.println("t1 트리");
		t1.print();
		System.out.println("===== t1에서 R 검색 =====");
		n = t1.BSTsearch("R");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		System.out.println("===== t1에서 C 검색 =====");
		n = t1.BSTsearch("C");
		if (n == null)
			System.out.println("Not Found");
		else
			System.out.println("Found");
		BinarySearchTree Small = new BinarySearchTree();
		BinarySearchTree Large = new BinarySearchTree();
		System.out.println("===== t 트리를 D를 기준으로 분할 =====");
		t.BSTsplit("D", Small, Large);
		System.out.println("D보다 작은 트리");
		Small.print();
		System.out.println("D보다 큰 트리");
		Large.print();
		System.out.println("===== t1 트리를 C를 기준으로 분할 =====");
		t1.BSTsplit("C", Small, Large);
		System.out.println("C보다 작은 트리");
		Small.print();
		System.out.println("C보다 큰 트리");
		Large.print();
		System.out.println("===== T를 루트로 하는 새로운 트리 생성 =====");
		t1 = new BinarySearchTree();
		t1.BSTinsert("T");
		t1.BSTinsert("U");
		t1.BSTinsert("S");
		t1.BSTinsert("R");
		t1.BSTinsert("O");
		t1.BSTinsert("M");
		t1.BSTinsert("W");
		t1.BSTinsert("X");
		t1.BSTinsert("C");
		t1.BSTinsert("B");
		t1.BSTinsert("A");
		System.out.println("T 삭제 전 트리");
		t1.print();
		System.out.println("===== T 삭제 =====");
		t1.BSTdelete("T");
		System.out.println("T 삭제 후 트리");
		t1.print();
		System.out.println("===== X, R 삭제 테스트를 위한 새로운 트리 생성 =====");
		t1 = new BinarySearchTree();
		t1.BSTinsert("T");
		t1.BSTinsert("U");
		t1.BSTinsert("R");
		t1.BSTinsert("S");
		t1.BSTinsert("O");
		t1.BSTinsert("M");
		t1.BSTinsert("X");
		t1.BSTinsert("W");
		t1.BSTinsert("C");
		t1.BSTinsert("B");
		t1.BSTinsert("Y");
		System.out.println("삭제 전 트리");
		t1.print();
		System.out.println("===== X 삭제 =====");
		t1.BSTdelete("X");
		System.out.println("X 삭제 후 트리");
		t1.print();
		System.out.println("===== R 삭제 =====");
		t1.BSTdelete("R");
		System.out.println("R 삭제 후 트리");
		t1.print();
	}
}
