package q16_5;

/**
 * Q16_4
 * Suppose we have the following code:
 *  public class Foo {
 *      public Foo() { . . . }
 *      public void first() { ... }
 *      public void second() { ... }
 *      public void thirdQ { ... }
 *  }
 * The same instance of Foo will be passed to three different threads. ThreadA will call
 * first, threads will call second, and threadC will call third. Design a mechanism
 * to ensure that first is called before second and second is called before
 * third.
 */
public class ApplicationFooBad {
    public static void main(String[] args) {
        FooBad foo = new FooBad();

        MyThread thread1 = new MyThread(foo, "first");
        MyThread thread2 = new MyThread(foo, "second");
        MyThread thread3 = new MyThread(foo, "third");

        thread3.start();
        thread2.start();
        thread1.start();
    }
}
