package q16_5;

public class MyThread  extends Thread {
    private final String method;
    private final FooBad foo;

    public MyThread(FooBad foo, String method) {
        this.method = method;
        this.foo = foo;
    }

    public void run() {
        switch (method) {
            case "first":
                foo.first();
                break;
            case "second":
                foo.second();
                break;
            case "third":
                foo.third();
                break;
        }
    }
}
