public class rotateArray {
    public static void main(String[] args) {
        int[] numArray = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        rotate(numArray, k);

        for (int i = 0; i < numArray.length; i++) {
            System.out.print(numArray[i] + " ");
        }
    }

    public static void rotate(int[] array, int k) {
        int n = array.length;
        k = k % n; // In case k is greater than the length of the array

        // Reverse the entire array
        reverse(array, 0, n - 1);

        // Reverse the first k elements
        reverse(array, 0, k - 1);

        // Reverse the elements from k to the end
        reverse(array, k, n - 1);
    }

    public static void reverse(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }
}
