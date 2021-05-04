package q16_5;

public class ApplicationFoo {
    public static void main(String[] args) {
        Foo foo = new Foo();

        MyThread thread1 = new MyThread(foo, "first");
        MyThread thread2 = new MyThread(foo, "second");
        MyThread thread3 = new MyThread(foo, "third");

        thread3.start();
        thread2.start();
        thread1.start();
    }
}
