public class InsertionSort {
    public static void main(String[] args) {
        int[] list = {7, 3, 5, 2, 9};

        for (int i = 1; i < list.length; i++) {
            while (i > 0 && list[i] < list[i - 1]) {
                int previous = list[i - 1];
                int current = list[i];

                list[i] = previous;
                list[i - 1] = current;

                i--;
            }
        }



        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i]);
        }
    }
}
