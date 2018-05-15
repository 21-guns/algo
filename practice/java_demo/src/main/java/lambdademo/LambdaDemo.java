package lambdademo;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.function.BiFunction;
import java.util.function.Consumer;

public class LambdaDemo {
    public static void main(String[] args) {
        modifyCapturedVariables();
        functionAsAParameter();
    }

    public static void modifyCapturedVariables() {
        int[] x = { 5 };
        Consumer<Integer> addYtoX = y -> { x[0] += y; };
        addYtoX.accept(3);
        System.out.println(Arrays.toString(x));
    }

    BiFunction<Integer, Integer, Integer> makeSum() {
        return (a, b) -> a + b;
    }

    public static void functionAsAReturnValue() {

    }

    public static void functionAsAParameter() {
        Integer[] numbers = {1, 3, 2};
        Arrays.sort(numbers, (a, b) -> Integer.compare(b, a));
        System.out.println(Arrays.toString(numbers));
        for (int n: numbers) System.out.println(n);
        for (int i = 0; i < numbers.length; i++) {System.out.println(numbers[i]);}
        Arrays.stream(numbers).forEach(s -> System.out.println(s));
    }
}
