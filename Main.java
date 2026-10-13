public class Main {
    public static void main(String[] args) {
        int age = 21;
        String name = "Jai";
        float height = 5.9f;
        boolean isStudent = true;
        System.out.println("Name:" + name + ", Age:" + age + ", Height:" + height + ", Student:" + isStudent);
        if (age >= 18) {
            System.out.println(name + " is a adult.");
        }
        else if (age < 18) {
            System.out.println(name + " is not an adult.");
        }
        else {
            System.out.println("Invalid age.");
        }
        System.out.println("Hello, World!");
    }
}