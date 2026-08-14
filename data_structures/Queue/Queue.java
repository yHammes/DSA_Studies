public class Queue {
    private Node front;
    private Node rear;

    public Queue() {
        this.front = null;
        this.rear = null;
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
    }

    public Integer dequeue() {
        if (this.front == null) {
            return null;
        }
        int value = this.front.value;

        this.front = this.front.next;
        if (this.front == null) {
            this.rear = null;
        }

        return value;
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        Integer value = queue.dequeue();
        value = queue.dequeue();
        value = queue.dequeue();

        System.out.println(value);

    }
}
