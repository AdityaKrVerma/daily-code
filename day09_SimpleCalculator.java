// Simple Calculator

import java.util.Scanner;

public class day09_SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int first = scanner.nextInt();

        System.out.print("Enter second number: ");
        int second = scanner.nextInt();

        int sum = first + second;
        int difference = first - second;
        int product = first * second;
        int quotient = first / second;
        int remainder = first % second;

        System.out.println();
        System.out.println("Results");
        System.out.println("-------");
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);
        System.out.println("Remainder: " + remainder);
    }
}