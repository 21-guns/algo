package classdemo;

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
        System.out.println(employee.name);
        System.out.println(employee.position);

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


