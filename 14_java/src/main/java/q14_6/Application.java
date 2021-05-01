package q14_6;

public class Application {
    public static void main(String[] args) {
        CircularArray<Integer> arr = new CircularArray<Integer>(10);
        for (int i = 0; i < 10; i++) {
            arr.set(i, i + 1);
        }
        System.out.println("rotate 5");
        arr.rotate(5);
        for (int i = 0; i < 10; i++) {
            System.out.printf("[%d] : %d%n", i, arr.get(i));
        }
        System.out.println("rotate -6");
        arr.rotate(-6);
        for (Integer i : arr) {
            System.out.printf("%d%n", i);
        }
    }
}
