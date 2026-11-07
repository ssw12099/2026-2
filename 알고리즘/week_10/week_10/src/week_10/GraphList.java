package week_10;

public class GraphList {
	int n;
	int e;
	Node[] header;

	public GraphList(int noOfVertices) {
		n = noOfVertices;
		e = 0;
		header = new Node[n];
	}

	public void insertEdge(int i, int j) {
		// 코드 작성
		Node current = header[i];
        while (current != null) {
            if (current.vertex == j) {
                return;
            }
            current = current.link;
        }

        Node a = new Node();
        a.vertex = j;
        a.link = header[i];
        header[i] = a;

        if (i != j) {
            Node b = new Node();
            b.vertex = i;
            b.link = header[j];
            header[j] = b;
        }
        e++;

	}

	public void removeEdge(int i, int j) {
		// 코드 작성
		Node prev = null;
        Node current = header[i];
        while (current != null && current.vertex != j) {
            prev = current;
            current = current.link;
        }
        if (current == null) {
            return;
        }
        if (prev == null) {
            header[i] = current.link;
        } else {
            prev.link = current.link;
        }

        if (i != j) {
            prev = null;
            current = header[j];
            while (current != null && current.vertex != i) {
                prev = current;
                current = current.link;
            }
            if (current != null) {
                if (prev == null) {
                    header[j] = current.link;
                } else {
                    prev.link = current.link;
                }
            }
        }
        e--;

	}

	public int[] adjacency(int u) {
	 // 코드 작성
		int count = 0;
        Node current = header[u];
        while (current != null) {
            count++;
            current = current.link;
        }

        int[] adj = new int[count];
        current = header[u];
        for (int i = 0; i < count; i++) {
            adj[i] = current.vertex;
            current = current.link;
        }
        return adj;
    }

	 
}
