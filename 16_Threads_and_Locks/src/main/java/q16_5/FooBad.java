package q16_5;

import java.util.concurrent.locks.ReentrantLock;

public class FooBad {

    private final int pauseTime = 1000;
    private ReentrantLock lock1;
    private ReentrantLock lock2;

    public FooBad() {
        try {
            this.lock1 = new ReentrantLock();
            this.lock2 = new ReentrantLock();
            this.lock1.lock();
            this.lock2.lock();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void first() {
        try {
            System.out.printf("FooBad::first() [Thread-%d] Started Executing 1%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::first() [Thread-%d] Finished Executing 1%n", Thread.currentThread().getId());
            lock1.unlock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void second() {
        try {
            lock1.lock();
            lock1.unlock();
            System.out.printf("FooBad::second() [Thread-%d] Started Executing 2%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::second() [Thread-%d] Finished Executing 2%n", Thread.currentThread().getId());
            lock2.unlock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void third() {
        try {
            lock2.lock();
            lock2.unlock();
            System.out.printf("FooBad::third() [Thread-%d] Started Executing 3%n", Thread.currentThread().getId());
            Thread.sleep(pauseTime);
            System.out.printf("FooBad::third() [Thread-%d] Finished Executing 3%n", Thread.currentThread().getId());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
