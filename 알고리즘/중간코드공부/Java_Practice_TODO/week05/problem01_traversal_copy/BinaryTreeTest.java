// 5주차 1번: 이진 트리의 순회 및 복사 구현
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

class BTNode {

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

class BinaryTree {

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
        if (t != null) {
            theInorder(t.Lchild);
            System.out.print(t.data);
            theInorder(t.Rchild);
        }
    }

    private void thePreorder(BTNode t) {
        if (t != null) {
            System.out.print(t.data);
            thePreorder(t.Lchild);
            thePreorder(t.Rchild);
        }
    }

    private void thePostorder(BTNode t) {
        if (t != null) {
            thePostorder(t.Lchild);
            thePostorder(t.Rchild);
            System.out.print(t.data);
        }

    }

    private void inorderIter1() {
        Stack stack = new Stack();
        BTNode curr = root;

        while (curr != null || !stack.empty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.Lchild;
            }
            curr = (BTNode) stack.pop();
            System.out.print(curr.data);
            curr = curr.Rchild;
        }
    }

    private void preorderIter() {
        Stack stack = new Stack();
        if (root == null) {
            return;
        }
        stack.push(root);
        while (!stack.empty()) {
            BTNode curr = (BTNode) stack.pop();
            System.out.print(curr.data);
            if (curr.Rchild != null) {
                stack.push(curr.Rchild);
            }
            if (curr.Lchild != null) {
                stack.push(curr.Lchild);
            }
        }
    }

    public void levelorder() {
        Queue qu = new Queue();
        if (root == null) {
            return;
        }
        qu.enqueue(root);

        while (!qu.isEmpty()) {
            BTNode curr = (BTNode) qu.dequeue();
            System.out.print(curr.data);

            if (curr.Lchild != null)
                qu.enqueue(curr.Lchild);

            if (curr.Rchild != null)
                qu.enqueue(curr.Rchild);
        }
    }

    public BinaryTree copy() {
        BinaryTree nt = new BinaryTree();
        nt.root = theCopy(root);
        return nt;
    }

    private BTNode theCopy(BTNode t) {
        if (t == null){
            return null;
        }
            BTNode nN = new BTNode(t.data);
            nN.Lchild = theCopy(t.Lchild);
            nN.Rchild = theCopy(t.Rchild);

            return nN;
    }

    public boolean equals(BinaryTree tr) {

        return theEqual(this.root, tr.root);

    }

    private boolean theEqual(BTNode s, BTNode t) {
        if(s==null&&t==null){
            return true;
        }
        if(s==null||t==null){
            return false;
        }
        if(!s.data.equals(t.data)){
            return false;
        }
        return theEqual(s.Lchild, t.Lchild)&&theEqual(s.Rchild, t.Rchild);
        }


}

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
