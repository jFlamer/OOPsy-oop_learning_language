class Person {
    public String name;
    private int age;
    public void introduce() {
        System.out.println(("Hi, my name is " + this.name));
    }
    public void setAge(int newAge) {
        this.age = newAge;
    }
    public void showAge() {
        System.out.println(("I'm " + this.age));
    }
}
public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        p.name = "Alice";
        p.setAge(30);
        p.introduce();
        p.showAge();
        // p.age = 100; // powinno być niedozwolone!
    }
}