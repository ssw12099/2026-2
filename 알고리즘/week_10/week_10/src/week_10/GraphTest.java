package week_10;

public class GraphTest {
	public static void main(String args[]) {
		Graph gr = new Graph(6);
		gr.insertEdge(0, 1);
		gr.insertEdge(0, 2);
		gr.insertEdge(1, 2);
		gr.insertEdge(1, 3);
		gr.insertEdge(2, 3);
		gr.insertEdge(2, 4);
		gr.insertEdge(3, 4);
		gr.insertEdge(3, 5);
		gr.insertEdge(4, 5);
		gr.insertEdge(1, 5);
		System.out.println();
		int[] adj;
		for (int i = 0; i < 6; i++) {
			adj = gr.adjacency(i);
			System.out.print(i + ": ");
			for (int e : adj) {
				System.out.print(e + " ");
			}
			System.out.println();
		}
		System.out.println();
		System.out.println("====================");
		gr = new Graph(7);
		gr.insertEdge(0, 1);
		gr.insertEdge(0, 2);
		gr.insertEdge(0, 3);
		gr.insertEdge(1, 4);
		gr.insertEdge(2, 4);
		gr.insertEdge(2, 5);
		gr.insertEdge(3, 5);
		gr.insertEdge(4, 6);
		gr.insertEdge(5, 6);
		System.out.println();
		for (int i = 0; i < 7; i++) {
			adj = gr.adjacency(i);
			System.out.print(i + ": ");
			for (int e : adj) {
				System.out.print(e + " ");
			}
			System.out.println();
		}
	}
}
