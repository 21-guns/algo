package classdemo;

import java.util.ArrayList;
import java.util.List;

public class ClassDemo {
    final int months = 12;
    public String name;

    private static int nextId;
    public int Id;

    static {
        nextId = getLastDbId();
    }

    {
        nextId++;
        Id = nextId;
    }

    static int getLastDbId() {
        return 0;
    }

    public static void main(String[] args) {
        Employee employee = new Employee("Max", "Dev");
        Employee employee2 = new Employee("Max", "Dev");
        boolean equal1 = employee == employee2;
        System.out.println(employee.name);
        System.out.println(employee.position);
        System.out.println(equal1);

        Statistic statistic = new Statistic();
        Game heros = new Game("Heros");
        Game doom = new Game("Doom");

        heros.addListener(statistic);
        doom.addListener(statistic);

        heros.start();
        doom.start();

        System.out.println(statistic.lastName);
        System.out.println(statistic.startsCount);


    }

    NestedClass create() {
        return new NestedClass();
    }

    class NestedClass {

    }

    static class NestedStaticClass {

    }

    public ClassDemo(String name) {
        this.name = "unknown";
    }
}


class Man {
    public String name;

    public Man(String name) {
        this.name = name;
    }
}

class Employee extends Man {
    public String position;

    public Employee(String name) {
        super(name);
        this.position = "unknown";
    }

    public Employee(String name, String position) {
        super(name);
        this.position = position;
    }
}

interface GameListener {
    void gameStarted(String name);
}

class Game {
    private List<GameListener> listeners = new ArrayList<GameListener>();
    public void addListener(GameListener listener) {
        listeners.add(listener);
    }

    public String name;
    public void start() {
        for (GameListener listener: listeners) listener.gameStarted(name);
    }

    public Game(String name) {
        this.name = name;
    }
}

class Statistic implements GameListener {
    public int startsCount;
    public String lastName;

    public void gameStarted(String name) {
        startsCount ++;
        lastName = name;
    }
}
