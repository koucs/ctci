package q16_6;

import java.util.Random;

public class Foo {

    public Foo() {
    }

    public void pause() {
        Random random = new Random();
        try {
            Thread.sleep(random.nextInt(2000 - 500) + 500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public synchronized void methodA() {
        System.out.printf("[Thread-%d] Start method-A %n", Thread.currentThread().getId());
        pause();
        System.out.printf("[Thread-%d] End method-A %n", Thread.currentThread().getId());
    }

    public synchronized void methodB() {
        System.out.printf("[Thread-%d] Start method-B %n", Thread.currentThread().getId());
        pause();
        System.out.printf("[Thread-%d] End method-B %n", Thread.currentThread().getId());
    }

    public void methodC() {
        System.out.printf("[Thread-%d] Start method-C %n", Thread.currentThread().getId());
        pause();
        System.out.printf("[Thread-%d] End method-C %n", Thread.currentThread().getId());
    }

}
