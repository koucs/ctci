package q8_9;

import java.util.stream.IntStream;

public class Application {
  public static void main(String[] args) {
    Directory root = new Directory("root", null);
    IntStream.range(0, 5).forEach(i -> root.addEntry(new File("file" + i, root, "content" + i)));
    System.out.println(root.numberOfFiles()); // 5
    System.out.println(root.size()); // 40

    Directory sub1 = new Directory("sub1", root);
    IntStream.range(0, 10).forEach(i -> sub1.addEntry(new File("subFile" + i, sub1, "cnts" + i)));
    root.addEntry(sub1);
    System.out.println(root.numberOfFiles()); // 16
    System.out.println(root.size()); // 90
  }
}
