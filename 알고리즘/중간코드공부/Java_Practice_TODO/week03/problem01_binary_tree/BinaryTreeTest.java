// 3주차 1번: 이진 트리의 기본 연산 구현
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
          root = new BTNode(ltree.root,data,rtree.root);
     }

     public boolean isEmpty() {
          return root == null;
     }

     public BinaryTree leftSubTree() {
          BinaryTree tmp = new BinaryTree();
          if(!isEmpty()){
               tmp.root = root.Lchild;
          }
          return tmp;
     }

     public BinaryTree rightSubTree() {
          BinaryTree tmp = new BinaryTree();
          if(!isEmpty()){
               tmp.root = root.Rchild;
          }
          return tmp;

     }

     public String rootData() {
          if (isEmpty()) {
            return null;
        }
          return root.data;
     }

     public int calculate() {
          return theCalculate(root);

     }

     private int theCalculate(BTNode t) {
          if(t.Lchild==null&&t.Rchild==null){
               return Integer.parseInt(t.data);
          }
          int left = theCalculate(t.Lchild);
          int right = theCalculate(t.Rchild);

          switch (t.data) {
               case "+": return left + right;
               case "-": return left - right;
               case "*": return left * right;
               case "/": return left / right;
          }
          return 0;

     }

     public int height() {
          return theHeight(root);
     }

     private int theHeight(BTNode t) {
          if(t == null){
               return -1;
          }
          int left = theHeight(t.Lchild);
          int right = theHeight(t.Rchild);
          return Math.max(left, right)+1;
     }

     public void print0() {
          print0(root);
          System.out.println();
     }

     private void print0(BTNode t) {
          if(t == null){
               return;
          }
          if(t.Lchild==null&&t.Rchild==null){
               System.out.print(t.data);
               }else{
               System.out.print("(");
               print0(t.Lchild);
               System.out.print(t.data);
               print0(t.Rchild);
               System.out.print(")");
          }
     }

}

public class BinaryTreeTest {

     public static void main(String args[]) {

          BinaryTree btree;

          BinaryTree ltree;

          BinaryTree rtree;


          rtree = new BinaryTree(

                    new BinaryTree(), "1", new BinaryTree());

          ltree = new BinaryTree(

                    new BinaryTree(), "2", new BinaryTree());

          btree = new BinaryTree(ltree, "+", rtree);

          ltree = btree;

          rtree = new BinaryTree(

                    new BinaryTree(), "3", new BinaryTree());

          btree = new BinaryTree(ltree, "*", rtree);

          System.out.println("계산 결과 : " + btree.calculate());

          System.out.print("수식 출력 : ");

          btree.print0();

          System.out.println("트리의 높이 : " + btree.height());

     }

}
