package q16_4;

/**
 * Q16.4
 * Design a class which provides a lock only if there are no possible deadlocks,
 */
public class Application {
    public static void main(String[] args) {
        int[] reqA = {1, 2, 3, 4};
        int[] reqB = {1, 3, 5};
        int[] reqC = {7, 5, 9, 2};

        LockFactory lf = LockFactory.initialize(10);
        System.out.println(lf.declare(1, reqA));
        System.out.println(lf.declare(2, reqB));
        System.out.println(lf.declare(3, reqC));

        System.out.println(lf.getLock(1, 1));
        System.out.println(lf.getLock(1, 2));
        System.out.println(lf.getLock(2, 4));
    }
}
