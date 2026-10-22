// 2주차 3번: 배열을 이용한 리스트 구현
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

class ArrayList {

     private String[] data;

     private int size;

     public ArrayList() {

          // TODO 01: ArrayList() 직접 구현 (아래 throw 문장을 지우고 작성)
          data = new String[10];
          size = 0;
     }

     public void insert(String s, int i) {
          if (i < 0 || i > size) {
               return;
          }

          if (size == data.length) {
               String[] temp = new String[data.length * 2];

               for (int j = 0; j < size; j++) {
                    temp[j] = data[j];
               }

               data = temp;
          }
          for (int j = size; j > i; j--) {
               data[j] = data[j - 1];
          }
          data[i] = s;
          size++;
     }

     public void delete(int i) {

          for (int j = i; j < size - 1; j++) {
               data[j] = data[j + 1];
          }
          size--;
          data[size] = null;

     }

     public int search(String s) {

          for (int i = 0; i < size; i++) {
               if (data[i].equals(s))
                    return i;
          }
          return -1;

     }

     public void print() {

          for (int i = 0; i < size; i++) {
               System.out.println(data[i]);
          }

     }

}

public class Main {

     public static void main(String[] args) {

          ArrayList list = new ArrayList();

          list.insert("A", 0);

          list.insert("B", 1);

          list.insert("C", 2);

          System.out.print("초기 리스트: ");

          list.print();

          int i = list.search("C");

          System.out.println("C의 위치: " + i);

          list.insert("D", i);

          System.out.print("D 삽입 후: ");

          list.print();

          i = list.search("C");

          list.delete(i);

          System.out.print("C 삭제 후: ");

          list.print();

     }

}
