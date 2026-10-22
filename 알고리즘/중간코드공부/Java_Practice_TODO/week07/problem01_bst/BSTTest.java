// 7주차 1번: 이진 탐색 트리의 검색, 삽입, 삭제 및 분할 구현
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

class TreeNode {

    String key;

    TreeNode Lchild;

    TreeNode Rchild;

}

class BinarySearchTree {

    private TreeNode rootNode;

    public TreeNode BSTsearch(String K) {
        TreeNode curr = rootNode;

        while (curr != null) {
            int cmp = K.compareTo(curr.key);
            if(cmp==0)return curr;
            if(cmp<0){
                curr = curr.Lchild;
            }else{
                curr = curr.Rchild;
            }
        }
        return null;
    }

    public void BSTinsert(String K) {
        TreeNode nN = new TreeNode();
        nN.key = K; 

        if(rootNode == null){
            rootNode = nN;
            return;
        }
        TreeNode curr = rootNode;
        while (true) {
            int cmp = K.compareTo(curr.key);
            if(cmp == 0){
                return;
            }
            if(cmp<0){
                if(curr.Lchild == null) {
                    curr.Lchild = nN;
                    return;
                }
                curr = curr.Lchild;
            }
            else{
                if(curr.Rchild==null){
                    curr.Rchild = nN;
                    return;
                }
                curr = curr.Rchild;
            }
        }
    }

    private TreeNode maxNode(TreeNode root) {
        if(root == null) return null;
        while (root.Rchild != null) {
            root = root.Rchild;            
        }
        return root;
    }

    private TreeNode delete(TreeNode root, String K) {
        if(root==null)return null;
        int cmp = K.compareTo(root.key);

        if(cmp<0){
            root.Lchild = delete(root.Lchild, K);
        }else if(cmp>0){
            root.Rchild = delete(root.Rchild, K);
        }else{
            if(root.Lchild==null){
                return root.Rchild;
            }

            if(root.Rchild==null){
                return root.Lchild;
            }

            TreeNode pre = maxNode(root.Lchild);
            root.key = pre.key;
            root.Lchild = delete(root.Lchild, pre.key);
        }

        return root;
    }

    public void BSTdelete(String K) {

        rootNode = delete(rootNode, K);

    }

    public boolean BSTsplit(String x, BinarySearchTree SmallTree, BinarySearchTree LargeTree) {
        TreeNode sD = new TreeNode();
        TreeNode lD = new TreeNode();

        TreeNode sT = sD;
        TreeNode lt = lD;
        TreeNode curr = rootNode;

        boolean found = false;

        while(curr != null){
            int cmp = curr.key.compareTo(x);
            if(cmp<0){
                TreeNode next = curr.Rchild;

                sT.Rchild = curr;
                sT = curr;
                sT.Rchild = null;

                curr = next;
            }else if(cmp>0){
                TreeNode next = curr.Lchild;

                lt.Lchild = curr;
                lt = curr;
                lt.Lchild = null;

                curr = next;
            }else{
                found = true;

                sT.Rchild = curr.Lchild;
                lt.Lchild = curr.Rchild;

                curr.Lchild = null;
                curr.Rchild = null;
                break;
            }
        }
        SmallTree.rootNode = sD.Rchild;
            LargeTree.rootNode = lD.Lchild;
            rootNode = null;
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

public class BSTTest {

    public static void main(String args[]) {

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
