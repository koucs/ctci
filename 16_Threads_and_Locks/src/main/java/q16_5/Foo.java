package q16_5;

import java.util.concurrent.Semaphore;

public class Foo extends FooBad {

    private final int pauseTime = 1000;
    private Semaphore sem1;
    private Semaphore sem2;

    public Foo() {
        try {
            this.sem1 = new Semaphore(1);
            this.sem2 = new Semaphore(1);
            this.sem1.acquire();
            this.sem2.acquire();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void first() {
        try {
            System.out.printf("FooBad::first() [Thread-%d] Started Executing 1%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::first() [Thread-%d] Finished Executing 1%n", Thread.currentThread().getId());
            sem1.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void second() {
        try {
            sem1.acquire();
            sem1.release();
            System.out.printf("FooBad::second() [Thread-%d] Started Executing 2%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::second() [Thread-%d] Finished Executing 2%n", Thread.currentThread().getId());
            sem2.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void third() {
        try {
            sem2.acquire();
            sem2.release();
            System.out.printf("FooBad::third() [Thread-%d] Started Executing 3%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::third() [Thread-%d] Finished Executing 3%n", Thread.currentThread().getId());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
