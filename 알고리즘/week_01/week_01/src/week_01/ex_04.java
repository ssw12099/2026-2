package week_01;

public class ex_04 {
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
