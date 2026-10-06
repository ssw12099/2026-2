package week_05;

public class BTNode {
	String data;
	BTNode Lchild;
	BTNode Rchild;

	public BTNode() {
	}

	public BTNode(String dt) {
		data = dt;
		Lchild = null;
		Rchild = null;
	}

	public BTNode(BTNode lc, String dt, BTNode rc) {
		data = dt;
		Lchild = lc;
		Rchild = rc;
	}
}
