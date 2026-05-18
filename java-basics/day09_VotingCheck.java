import java.util.Scanner;

public class day09_VotingCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        if (age >= 18) {
            System.out.println("You can vote");
        } else {
            System.out.println("You cannot vote yet");
        }

        scanner.close();
    }
}