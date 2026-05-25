import java.util.Scanner;

public class day09_SmartProfileCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your full name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Enter your marks: ");
        int marks = scanner.nextInt();

        boolean isAdult = age >= 18;

        System.out.println();
        System.out.println("Result");
        System.out.println("------");

        if (name.equalsIgnoreCase("Aditya Kumar Verma")) {
            System.out.println("Name matched");
        } else {
            System.out.println("Name not matched");
        }

        if (isAdult) {
            System.out.println("You are an adult");
        } else {
            System.out.println("You are not an adult yet");
        }

        if (marks < 0 || marks > 100) {
            System.out.println("Invalid marks");
        } else if (marks >= 90) {
            System.out.println("Grade A");
        } else if (marks >= 80) {
            System.out.println("Grade B");
        } else if (marks >= 70) {
            System.out.println("Grade C");
        } else if (marks >= 40) {
            System.out.println("Pass");
        } else {
            System.out.println("Fail");
        }

        scanner.close();
    }
}