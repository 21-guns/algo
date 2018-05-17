package controldemo;

public class SwitchDemo {
    public static void main(String[] args) {
        caseDemo();
    }

    private static void caseDemo() {
        String str;
        int monitorInchSize = 24;
        switch (monitorInchSize) {
            case 15:
                str = "too small";
                break;
            case 16: case 17: case 18:
                str = "good";
                break;
            case 19: case 20: case 21: case 22: case 23:
                str = "work";
                break;
            case 24: case 25: case 26:
                str = "choice";
                break;
            default:
                str = "";
        }
        System.out.println(str);
    }
}
