package controldemo;

public class InterruptionDemo {
    public static void main(String[] args) {
//        breakDemo();
//        continueDemo();
//        returnDemo();
        labeledDemo();
    }

    private static void breakDemo() {
        for (; ; ) {
            System.out.println("Endless Cycle");
            break;
        }
    }

    private static void continueDemo() {
        for (; ; ) {
            System.out.println("Endless Cycle");
            continue;
        }
    }

    private static void returnDemo() {
        for (; ; ) {
            System.out.println("Endless Cycle");
            return;
        }
    }

    private static void labeledDemo() {
        int firstMatchValue = -1;
        int[] array1 = {1, 2, 3};
        int[] array2 = {2, 3, 4};

        firstLoop: for (int value1: array1) {
            for (int value2: array2) {
                if (value1 == value2) {
                    firstMatchValue = value2;
                    break firstLoop;
                }
            }
        }
        System.out.println(firstMatchValue);
    }
}
