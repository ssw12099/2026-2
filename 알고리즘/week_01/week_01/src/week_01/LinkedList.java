package week_01;

public class LinkedList {
	private Node head;
	private int size;

	public LinkedList() {
		// 코드 작성
		head = null;
		size = 0;
	}

	public void addFirst(String s) {
		// 코드 작성
		Node nNode = new Node(s);

		nNode.next = head;
		head = nNode;

		size++;
	}

	public void insert(String s, Node p) {
		// 코드 작성
		Node nNode = new Node(s);

		nNode.next = p.next;
		p.next = nNode;

		size++;
	}

	public void delete(Node p) {
		// 코드 작성
		if (p != null && p.next != null) {
			p.next = p.next.next;
			size--;
		}
	}

	public Node search(String s) {
		// 코드 작성
		Node p = head;

		while (p != null) {
			if (p.data.equals(s)) {
				return p;
			}

			p = p.next;
		}

		return null;
	}

	public void print() { // 코드 작성
		Node p = head;
		System.out.print("LinkedList = { ");

		while (p.next != null) {
			System.out.print(p.data + " ");	
			p = p.next;
		}
		System.out.println(p.data + " }");
	}
}
