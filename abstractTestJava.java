abstract class Animal {
    abstract public void speak();
    final public void info() {
        System.out.println("I'm an animal");
    }
}
class Dog extends Animal {
    public void speak() {
        System.out.println("Woof!");
    }
}
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.speak();
        d.info();
    }
}