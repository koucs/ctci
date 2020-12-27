package q8_5;

import java.util.HashMap;
import java.util.stream.IntStream;

public class Application {
  public static void main(String[] args) {
    OnlineReaderSystem system = new OnlineReaderSystem();
    UserManager um = system.getUserManager();
    BookLibrary bl = system.getBookLibrary();

    IntStream.range(1, 11).boxed().forEach(i -> um.addUser(i, "User-" + i, 1));
    IntStream.range(1, 11).boxed().forEach(i -> bl.addBook(i, "Book-" + i));

    system.setActiveUser(um.find(1));
    system.setActiveBook(bl.find(5));

    System.out.println("=== refresh ===");
    system.getDisplay().refreshUsername();
    system.getDisplay().refreshTitle();
  }
}
