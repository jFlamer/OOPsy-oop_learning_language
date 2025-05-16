class Person {
    public String name;
    public int age;
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public void introduce() {
        System.out.println(("Hi, my name is " + this.name));
    }
}
class Student extends Person {
    public boolean isGraduated;
    public Student(String name, int age, boolean isGraduated) {
        super(name, age);
        this.isGraduated = isGraduated;
    }
    public void status() {
        if (this.isGraduated) {
        System.out.println((this.name + " has graduated."));
        }
        else {
        System.out.println((this.name + " is still studying."));
        }
    }
}
public class Main {
    public static void main(String[] args) {
        Student alice = new Student("Alice", 22, false);
        alice.introduce();
        alice.status();
        do {
        System.out.println(("Age: " + alice.age));
        alice.age = (alice.age + 1);
        } while (!(alice.age > 24));
        var numbers = java.util.Arrays.asList(1, 2, 3);
        for (Object n : numbers) {
        System.out.println(("Liczba: " + n));
        }
        return;
    }
}