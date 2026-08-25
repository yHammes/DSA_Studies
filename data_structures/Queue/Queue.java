public class Queue {
    private Node front;
    private Node rear;
    private int size;

    public Queue() {
        this.front = null;
        this.rear = null;
        this.size = 0;
    }

    public void enqueue(int value) {
        Node newNode = new Node(value);
        if (this.rear == null) {
            this.front = newNode;
            this.rear = newNode;
        } else {
            this.rear.next = newNode;
            this.rear = newNode;
        }
        this.size++;
    }

    public Integer dequeue() {
        if (this.isEmpty()) {
            return null;
        }
        int value = this.front.value;

        this.front = this.front.next;
        if (this.isEmpty()) {
            this.rear = null;
        }


        this.size--;
        return value;
    }

    public boolean isEmpty() {
        return this.front == null;
    }

    public int size() {
        return this.size;
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        System.out.println("Size: " + queue.size());
        Integer value = queue.dequeue();
        value = queue.dequeue();
        value = queue.dequeue();

        System.out.println(value);

    }
}
