package q16_6;

/**
 * Q16.6
 * You are given a class with synchronized method A and a normal method C.
 * If you have two threads in one instance of a program, can they both execute A at the same time?
 * Can they execute A and C at the same time?
 */
public class Application {
    public static void main(String[] args) {
        /* Part 1 Demo -- same instance */
        System.out.println("[Execute A at the same time] Same Foo instance");
        Foo fooA = new Foo();
        MyThread thread1a = new MyThread(fooA, "A");
        MyThread thread2a = new MyThread(fooA, "A");
        thread1a.start();
        thread2a.start();
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("\n\n");

        System.out.println("[Execute A at the same time] Difference Foo instances");
        Foo fooB1 = new Foo();
        Foo fooB2 = new Foo();
        MyThread thread1b = new MyThread(fooB1, "A");
        MyThread thread2b = new MyThread(fooB2, "A");
        thread1b.start();
        thread2b.start();
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("\n\n");

        System.out.println("[Execute A and C at the same time] Same Foo instance");
        Foo fooC = new Foo();
        MyThread thread1c = new MyThread(fooC, "A");
        MyThread thread2c = new MyThread(fooC, "C");
        thread1c.start();
        thread2c.start();
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("\n\n");

        System.out.println("[Execute A and B at the same time] Same Foo instance");
        Foo fooD = new Foo();
        MyThread thread1d = new MyThread(fooD, "A");
        MyThread thread2d = new MyThread(fooD, "B");
        thread1d.start();
        thread2d.start();
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("\n\n");

    }

}

class MyThread extends Thread {
    private final Foo foo;
    private final String firstMethodName;

    public MyThread(Foo foo, String firstMethodName) {
        this.foo = foo;
        this.firstMethodName = firstMethodName;
    }

    public void run() {
        if (this.firstMethodName.equals("A")) {
            this.foo.methodA();
        } else if (this.firstMethodName.equals("C")) {
            this.foo.methodC();
        } else {
            this.foo.methodB();
        }
    }
}
