package week_10;

public class DiGraph {
	int n;
	int e;
	int[][] weight;

	public DiGraph(int noOfVertices) {
		n = noOfVertices;
		e = 0;
		weight = new int[n][n];
	}

	public void insertEdge(int i, int j) {
		// 코드 작성
		if (weight[i][j] == 0) {
            weight[i][j] = 1;
            e++;
        }

	}

	public void removeEdge(int i, int j) {
		// 코드 작성
		 if (weight[i][j] != 0) {
	            weight[i][j] = 0;
	            e--;
	        }

	}

	public int[] successor(int u) {
		// 코드 작성
		 int count = 0;
	        for (int i = 0; i < n; i++) {
	            if (weight[u][i] != 0) {
	                count++;
	            }
	        }

	        int[] adj = new int[count];
	        int index = 0;
	        for (int i = 0; i < n; i++) {
	            if (weight[u][i] != 0) {
	                adj[index++] = i;
	            }
	        }
	        return adj;
	    }

	}

