package regexdemo;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexDemo {
    public static void main(String[] args) {

        regexMatch();
        regexOption();
        regexSearchAll();
        regexSub();
        regexSearchForMatch();
    }

    private static void regexMatch() {
        String data1 = "aaab";
        String data2 = "aaaba";
        String pattern = "a+b";

        Pattern p = Pattern.compile(pattern);
        Matcher m1 = p.matcher(data1);
        boolean b1 = m1.matches();

        Matcher m2 = p.matcher(data2);
        boolean b2 = m2.matches();

        System.out.println(b1);
        System.out.println(b2);
    }

    private static void regexOption() {
        String data = "AaaA\r\naaaA";
        String pattern = "^(a+)$";

        Pattern p = Pattern.compile(pattern, Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
        Matcher m = p.matcher(data);
        m.find();
        String value = m.group(0);
        System.out.println(value);
    }

    private static void regexSearchAll() {
        String data = "Pi = 3.14, exponent = 2.718";
        String pattern = "\\d+\\.\\d+";
        Pattern p = Pattern.compile(pattern);

        Matcher m = p.matcher(data);
        List<String> allMatchers = new ArrayList<String>();
        while (m.find()) {
            allMatchers.add(m.group(0));
        }

        allMatchers.stream().forEach(s -> System.out.println(s));

    }

    private static void regexSub() {
        String data = "Pi = 3.14, exponent = 2.718";
        String pattern = "\\d+\\.\\d+";
        data = data.replaceAll(pattern, "<f>$0</f>");
        System.out.println(data);
    }

    private static void regexSearchForMatch() {
        String data = "Pi = 3.14, exponent = 2.718";
        String pattern = "\\d+\\.\\d+";
        Pattern p = Pattern.compile(pattern);

        Matcher m = p.matcher(data);
        if (m.find()) {
            Double pi = Double.parseDouble(m.group(0));
            System.out.println(pi);
        }
    }
}
