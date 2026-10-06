package week_05;

public class Queue {
	private int front;
	private int back;
	private Object[] data;
	private final static int MAX = 100;

	public Queue() {
		data = new Object[MAX];
		front = back = 0;
	}

	public int size() {
		if (back >= front)
			return back - front;
		else
			return MAX + back - front;
	}

	public boolean isEmpty() {
		return front == back;
	}

	public void enqueue(Object x) {
		back = (back + 1) % MAX;
		if (back == front) {
		}
		data[back] = x;
	}

	public Object dequeue() {
		front = (front + 1) % MAX;
		return data[front];
	}

	public Object front() {
		return data[(front + 1) % MAX];
	}
}
