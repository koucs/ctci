package q16_3.soulution2;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Chopstick {
    private final Lock lock;
    private final int num;

    public Chopstick(int n) {
        lock = new ReentrantLock();
        num = n;
    }

    public void pickUp() {
        lock.lock();
    }

    public void putDown() {
        lock.unlock();
    }

    public int getNum() {
        return num;
    }
}
