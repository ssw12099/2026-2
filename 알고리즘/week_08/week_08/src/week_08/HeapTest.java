package week_08;

public class HeapTest {
	public static void main(String args[]) {
		 Heap h = new Heap();
		 System.out.println("insert()로 하나씩 삽입해서 만든 힙 테스트");
		 h.insert("30");
		 h.insert("40");
		 h.insert("20");
		 h.insert("10");
		 h.insert("35");
		 h.insert("45");
		 h.insert("50");
		 h.insert("25");
		 h.insert("70");
		 h.insert("48");
		 h.insert("64");
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println(h.delete());
		 System.out.println("--------------------------------------------");
		 System.out.println("배열 전체를 생성자에 넣어 한 번에 만든 힙 테스트");
		 String[] sk = {"30", "50", "55", "90", "30", "70", "60", "25", "80", "40", "45", "35", "47", "57", "38", "88"};
		 h = new Heap(sk);
		 for (int i = 1; i < 16; i++)
		 System.out.println(h.delete());
		 }
}
