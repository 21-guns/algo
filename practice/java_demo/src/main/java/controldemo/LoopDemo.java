package controldemo;

public class LoopDemo {
    public static void main(String[] args) {
//        endlessCycle();
        forIn();
        doWhile();
        forDemo();
        whileDemo();
    }

    private static void endlessCycle() {
        for (;;) {
            System.out.println("Endless Cycle");
        }

//        while (true) {
//            System.out.println("Endless Cycle");
//        }
//
//        do {
//            System.out.println("Endless Cycle");
//        } while (true);
    }

    private static void forIn() {
        int [] numbers = {2, 3, 4, 5, 6, 7};
        for (int number: numbers) {
            System.out.println(number);
        }
    }

    private static void doWhile() {
        int i = 7;
        int f7 = 1;
        do {
            f7 *= i;
            i--;
        } while (i > 1);
        System.out.println(f7);
    }

    private static void forDemo() {
        int [] numbers = {2, 3, 4, 5, 6, 7};
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }

    private static void whileDemo() {
        int i = 7;
        int f7 = 1;
        while (i > 1) {
            f7 *= i;
            i--;
        }
        System.out.println(f7);
    }

}
