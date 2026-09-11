package week_01;

public class ex_03 {

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
