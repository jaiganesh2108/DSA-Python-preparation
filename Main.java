import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
         
         System.out.println("== Student informations ==");

         String name = input.nextLine();
         int age = input.nextInt();

         System.out.println("Name:" + name);
         System.out.println("Age:" + age);

    }
}