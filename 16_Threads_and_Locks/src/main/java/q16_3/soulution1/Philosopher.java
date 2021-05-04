package q16_3.soulution1;

import java.util.Random;

public class Philosopher extends Thread {
    private static final int bites = 10;
    private final Chopstick left, right;
    private final int num;

    public Philosopher(Chopstick left, Chopstick right, int num) {
        this.left = left;
        this.right = right;
        this.num = num;
    }

    public boolean pickUp() {
        if (!this.left.pickUp()) {
            return false;
        }
        if (!this.right.pickUp()) {
            this.left.putDown();
            return false;
        }
        return true;
    }

    public void chew() {
        System.out.printf("Philosophy-%d [Thread-%d] Now Eating %n", this.num, Thread.currentThread().getId());
        pause();
    }

    public void pause() {
        Random random = new Random();
        try {
            Thread.sleep(random.nextInt(500 - 400) + 400);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void putDown() {
        this.right.putDown();
        this.left.putDown();
    }

    public void eat() {
        System.out.printf("Philosophy-%d [Thread-%d] Start Eating %n", this.num, Thread.currentThread().getId());
        if (pickUp()) {
            chew();
            putDown();
            System.out.printf("Philosophy-%d [Thread-%d] End Eating %n", this.num, Thread.currentThread().getId());
        } else {
            System.out.printf("Philosophy-%d [Thread-%d] Give Up Eating %n", this.num, Thread.currentThread().getId());
        }
    }

    public void run() {
        for (int i = 0; i < bites; i++) {
            eat();
        }
    }
}
