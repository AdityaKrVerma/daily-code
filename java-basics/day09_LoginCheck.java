import java.util.Scanner;

public class day09_LoginCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final int CORRECT_PIN = 1234;

        System.out.print("Enter PIN: ");
        int enteredPin = scanner.nextInt();

        if (enteredPin == CORRECT_PIN) {
            System.out.println("Login successful");
        } else {
            System.out.println("Incorrect PIN");
        }

        scanner.close();
    }
}