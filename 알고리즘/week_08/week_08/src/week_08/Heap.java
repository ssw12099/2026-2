package week_08;

public class Heap {
		 private int count;
		 private int size;
		 private String[] itemArray;
		 public Heap() {
		 count = 0;
		 size = 64;
		 itemArray = new String[size];
		 }
		 public Heap(String[] origArray) {
			    count = 0;
			    size = Math.max(64, origArray.length);
			    itemArray = new String[size];

			    for (int i = 1; i < origArray.length; i++) {
			        insert(origArray[i]);
			    }
			}
		 public void insert(String newItem) {
			    if (count + 1 >= size) {
			        size *= 2;
			        String[] temp = new String[size];
			        System.arraycopy(itemArray, 0, temp, 0, count + 1);
			        itemArray = temp;
			    }

			    int i = ++count;

			    while (i > 1 && itemArray[i / 2].compareTo(newItem) < 0) {
			        itemArray[i] = itemArray[i / 2];
			        i /= 2;
			    }

			    itemArray[i] = newItem;
			}
		 public String delete() {
			    if (count == 0) {
			        return null;
			    }

			    String max = itemArray[1];
			    String last = itemArray[count];
			    itemArray[count] = null;
			    count--;

			    int parent = 1;
			    int child = 2;

			    while (child <= count) {
			        if (child < count &&
			            itemArray[child].compareTo(itemArray[child + 1]) < 0) {
			            child++;
			        }

			        if (last.compareTo(itemArray[child]) >= 0) {
			            break;
			        }

			        itemArray[parent] = itemArray[child];
			        parent = child;
			        child = parent * 2;
			    }

			    if (count > 0) {
			        itemArray[parent] = last;
			    }

			    return max;
			}
		
}
