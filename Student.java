import java.util.Scanner;

public class Student {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Enter the Name of the Student:");
        String Name = scn.nextLine();
        System.out.print("Enter the Score of the Student for 100 Marks:");
        double Score = scn.nextDouble();
        scn.nextLine();
        System.out.print("Enter the Department of the Student:");
        String department = scn.nextLine();
        scn.close();

        double Mark = Score / 10;
        System.out.println("Name:" + Name);
        System.out.println("Score:" + Score);
        System.out.println("Department:" + department);
        System.out.println("Mark:" + Mark);

        int age = 20;
        int newage = 20;
        if (age == newage) {
            System.out.println("Age is equal to 20");
        }
        else {
            System.out.println("Age is not equal to 20");
        }
    }
}