import java.util.Scanner;
class User {
    public String name;
    public int age;
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public void greet() {
        System.out.println(("Hello, " + this.name));
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        User user = new User("Unknown", 0);
        System.out.print("What is your name? ");
        user.name = scanner.nextLine();
        System.out.print("How old are you? ");
        user.age = Integer.parseInt(scanner.nextLine());
        user.greet();
        System.out.println((("You are " + user.age) + " years old."));
        return;
    }
}