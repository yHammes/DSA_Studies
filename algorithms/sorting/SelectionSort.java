public class SelectionSort {
    public static void main(String[] args) {
        int[] list = {7, 4, 3, 5, 1, 2, 9, 8, 6};

        for (int i = 0; i < list.length; i++) {
            for (int j = 0 + i + 1; j < list.length; j++) {
                if (list[i] > list[j]) {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }

        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i]);
        }
    }
}
