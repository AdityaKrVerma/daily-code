// Create SimpleMath.java with one class and two methods.

public class day08_SimpleMath {

    public static int add(int a, int b) {
        return a + b;
    }

    public static int subtract(int a, int b) {
        return a - b;
    }

    public static void main(String[] args) {
        System.out.println("Sum: " + add(10, 5));        // Outputs: Sum: 15
        System.out.println("Difference: " + subtract(10, 5)); // Outputs: Difference: 5
    }
}