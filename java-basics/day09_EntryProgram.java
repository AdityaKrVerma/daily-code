import java.util.Scanner;

public class day09_EntryProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Do you have ID? true/false: ");
        boolean hasId = scanner.nextBoolean();

        if (age >= 18 && hasId) {
            System.out.println("Entry allowed");
        } else {
            System.out.println("Entry denied");
        }

        scanner.close();
    }
}