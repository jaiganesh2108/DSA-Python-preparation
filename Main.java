import java.util.Scanner;
import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
         
        System.out.println("== Student informations ==");
        System.out.print("Enter name: ");
        String name = input.nextLine();
        System.out.print("Enter age: ");
        int age = input.nextInt();

        if(name.isEmpty() || age <= 0 || age >= 150) {
            System.out.println("Invalid input. Please enter the valid details.");
            input.close();
            return;
        }

        // PostgreSQL connection details
        String url = "jdbc:postgresql://localhost:8011/student_db";
        String username = "postgres";
        String password = "your_password"; // Replace with your actual password

        String sql = "INSERT INTO students (name, age) VALUES (?, ?)";

        try (
            Connection connection = DriverManager.getConnection(url, username, password);
            PreparedStatement statement = connection.prepareStatement(sql)) {
                statement.setString(1, name);
                statement.setInt(2, age);

                int rows = statement.executeUpdate();

                if (rows > 0) {
                    System.out.println("table updated successfully.");
                }
            }

        catch (SQLException e) {
            System.out.println("Error connecting to the database: " + e.getMessage());
        }
    input.close();
    }
}