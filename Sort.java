

class Sort {
    static public long[] selectionSort(long[] arr) {
        if (arr.length == 0) {
            return null;
        } else if (arr.length == 1) {
            return arr;
        } else {
            for (int i = 0; i < arr.length; i++) {
                for (int j = i; j < arr.length; j++) {
                    if (arr[i] > arr[j]) {
                        long temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
            return arr;
        }

    }

    static public long[] bubbleSort(long[] arr) {
        if (arr.length == 0) {
            return null;
        } else if (arr.length == 1) {
            return arr;
        } else {
            boolean flag = true;
            long i = 0;

            while (flag) {
                flag = false;
                for (int j = 0; j < arr.length - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        long temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                    flag = true;
                }
                i++;
            }
            return arr;
        }
    }

    static public long[] insertionSort(long[] arr) {
        if (arr.length == 0) {
            return null;
        } else if (arr.length == 1) {
            return arr;
        } else {
            for (int i = 1; i < arr.length; i++) {
                long x = arr[i];
                int j = i - 1;

                while (j >= -1 && arr[j] > x) {
                    arr[j + 1] = arr[j];
                    j--;

                }
                arr[j + 1] = x;
            }
            return arr;

        }
    }

    static public int partition(long[] arr, int low, int high) {

        long pivot = arr[low];
        int i = low, j = high;

        do {
            do {
                i++;
            } while (arr[i] <= pivot);
            do {
                j--;
            } while (arr[i] > pivot);
            if (i < j) {
                long temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        } while (i < j);

        long temp = arr[low];
        arr[low] = arr[j];
        arr[j] = temp;

        return j;
    }

    

    static public void quickSort(long[] arr, int low, int high) {
        if (low < high) {
            int j = partition(arr, low, high);

            quickSort(arr, low, j - 1);
            quickSort(arr, j + 1, high);
        }
    }

    public static void main(String args[]) {

        long arr_selection[] = new long[] { 5687, 64225, 62581, 645234, 5452545, 565846125, 2565245, 25, 45, 5, 6,
                9559545, 6, 855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 412556514, 41552, 55 };

        arr_selection = selectionSort(arr_selection);

        System.out.println("for selection sort......");

        for (int i = 0; i < arr_selection.length; i++) {
            System.out.print(arr_selection[i] + " ");
        }

        long arr_bubble[] = new long[] { 5687, 64225, 62581, 645234, 5452545, 565846125, 2565245, 25, 45, 5, 6, 9559545,
                6, 855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 412556514, 41552, 55 };

        arr_bubble = bubbleSort(arr_bubble);

        System.out.println();

        System.out.println("for bubble sort......");

        for (int i = 0; i < arr_bubble.length; i++) {
            System.out.print(arr_bubble[i] + " ");
        }

        long arr_insertion[] = new long[] { 5687, 64225, 62581, 645234, 5452545, 565846125, 2565245, 25, 45, 5, 6,
                9559545, 6, 855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 412556514, 41552, 55 };

        arr_insertion = bubbleSort(arr_insertion);

        System.out.println();

        System.out.println("for insertion sort......");

        for (int i = 0; i < arr_insertion.length; i++) {
            System.out.print(arr_insertion[i] + " ");
        }

        long arr_quick_sort[] = new long[] { 5687, 64225, 62581, 645234, 5452545, 565846125, 2565245, 25, 45, 5, 6,
                9559545, 6, 855121, 5421512, 412, 54212, 41, 5, 15, 1215, 4212, 5112545, 1215, 412556514, 41552, 55 };

        quickSort(arr_quick_sort, 0, arr_quick_sort.length - 1);

        System.out.println();

        System.out.println("for quick sort sort......");

        for (int i = 0; i < arr_quick_sort.length; i++) {
            System.out.print(arr_quick_sort[i] + " ");
        }

    }
}