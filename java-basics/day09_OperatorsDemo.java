// Program covering Operators, Precedence and String

public class day09_OperatorsDemo {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        System.out.println("Arithmetic");
        System.out.println("----------");
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));

        int score = 50;
        score += 10;
        score *= 2;

        System.out.println();
        System.out.println("Score: " + score);

        int age = 20;
        boolean hasId = true;
        boolean isMember = false;

        boolean canEnter = age >= 18 && hasId;
        boolean getsDiscount = isMember || age < 18;
        boolean needsSignup = !isMember;

        System.out.println();
        System.out.println("Logical Results");
        System.out.println("---------------");
        System.out.println("Can enter: " + canEnter);
        System.out.println("Gets discount: " + getsDiscount);
        System.out.println("Needs signup: " + needsSignup);

        System.out.println();
        System.out.println("Precedence");
        System.out.println("----------");
        System.out.println(10 + 5 * 2);
        System.out.println((10 + 5) * 2);

        System.out.println();
        System.out.println("String trap");
        System.out.println("-----------");
        System.out.println("Result: " + 10 + 20);
        System.out.println("Result: " + (10 + 20));
    }
}