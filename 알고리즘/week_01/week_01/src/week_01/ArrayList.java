package week_01;

public class ArrayList {
	private String[] data;
	private int size;
	private final int ArraySize = 15;

	public ArrayList() {
		data = new String[ArraySize];
		size = 0;
	}

	public void insert(String s, int i) {
		// 코드 작성
		if(i >= size || i<0) System.out.println("잘못된 인덱스");
		if(size >= ArraySize) System.out.println("insert 오버플로");
		for (int j = size; j > i; j--) {
	            data[j] = data[j - 1];
	        }
		 data[i] = s;
		 size++;
	}

	public void delete(int i) {
		if(i >= ArraySize || i<0) System.out.println("잘못된 인덱스");
		for (int j = i; j < size - 1; j++) {
            data[j] = data[j + 1];
        }

        size--;
	}

	public int search(String s) {
		// 코드 작성
		for (int i = 0; i < size; i++) {
            if (data[i].equals(s)) {
                return i;
            }
        }
		return -1;
	}

	public void print() {
		// 코드 작성
		System.out.print("ArrList = { ");
		for (int i = 0; i < size-1; i++) {
			System.out.print(data[i]+" ");
		}
		System.out.println(data[size - 1]+" }");
        
	}
}
