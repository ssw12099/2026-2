// 2주차 4번: 연결 표현을 이용한 리스트 구현
// 제공된 PDF의 기본 코드 및 main() 보존 / 구현할 함수만 TODO 처리
// TODO에 들어 있는 throw는 임시 표시이므로, 직접 구현할 때 삭제하세요.

class Node {

    String data;

    Node next;

    public Node(String data) {
        this.data = data;
        this.next = null;
    }

}

class LinkedList {

    private Node head;

    @SuppressWarnings("unused")
    private int size;

    public LinkedList() {
        head = null;
        size = 0;
    }

    public void addFirst(String s) {
        Node newN = new Node(s);
        newN.next = head;
        head = newN;
        size++;
    }

    public void insert(String s, Node p) {
        if (p == null) {
            return;
        }
        Node newN = new Node(s);
        newN.next = p.next;
        p.next = newN;
        size++;
    }

    public void delete(Node p) {
        if (p == null || head == null) {
            return;
        }
        if (head == p) {
            head = head.next;
            size--;
            return;
        }
        Node curr = head;

        while (curr.next != null) {
            if (curr.next == p)
                break;
            curr = curr.next;
        }
        if (curr.next == null) {
            return;
        }
        curr.next = curr.next.next;
        size--;

    }

    public Node search(String s) {
        Node curr = head;
        while (curr != null) {
            if (curr.data.equals(s))
                return curr;
            curr = curr.next;
        }
        return null;
    }

    public void print() {
        Node curr = head;
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.next;
        }

    }

}

public class Main {

    public static void main(String[] args) {

        LinkedList list = new LinkedList();

        list.addFirst("C");

        list.addFirst("B");

        list.addFirst("A");

        list.print();

        Node n = list.search("B");

        list.insert("D", n);

        list.print();

        list.delete(n);

        list.print();

    }

}
