package controldemo;

public class ConditionDemo {
    public static void main(String[] args) {
        ifDemo();
    }

    private static void ifDemo() {
        int n = -42;
        String classify = (n > 0)? "positive" : "negative";
        System.out.println(classify);

        if (classify == "positive") {
            System.out.println("Smile");
        } else if (classify == "negative") {
            System.out.println("Hehe");
        } else {
            System.out.println("Wa");
        }
    }
}
