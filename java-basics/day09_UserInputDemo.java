// Program using different input types

import java.util.Scanner;

public class day09_UserInputDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Enter your height: ");
        double height = scanner.nextDouble();

        System.out.print("Are you learning Java? true/false: ");
        boolean isLearningJava = scanner.nextBoolean();

        System.out.println();
        System.out.println("Profile");
        System.out.println("-------");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Learning Java: " + isLearningJava);
    }
}