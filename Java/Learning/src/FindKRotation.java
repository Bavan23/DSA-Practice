public class FindKRotation {

    public static void main(String[] args) {

        // 🔹 Default input
        int[] arr = {15, 18, 2, 3, 6};
        int n = arr.length;

        FindKRotation obj = new FindKRotation();
        int rotations = obj.findKRotation(arr, n);

        System.out.println("Rotation count = " + rotations);
    }

    // Function to find rotation count
    int findKRotation(int arr[], int n) {
        int pivot = findPivot(arr);

        // array not rotated
        if (pivot == -1) {
            return 0;
        }
        return pivot + 1;
    }

    // Binary search to find pivot
    int findPivot(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            // case 1: pivot found
            if (mid < end && arr[mid] > arr[mid + 1]) {
                return mid;
            }

            // case 2: pivot found
            if (mid > start && arr[mid] < arr[mid - 1]) {
                return mid - 1;
            }

            // case 3: decide search side
            if (arr[start] >= arr[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
}