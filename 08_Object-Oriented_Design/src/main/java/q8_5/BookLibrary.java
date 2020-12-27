package q8_5;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import java.util.HashMap;

public class BookLibrary {
  private final HashMap<Integer, Book> books = new HashMap<>();

  @Nullable
  public Book addBook(int id, @Nonnull String name) {
    if (books.containsKey(id)) {
      return null;
    }
    Book b = Book.builder().ID(id).name(name).build();
    books.put(id, b);
    return b;
  }

  public boolean remove(User user) {
    return remove(user.getID());
  }

  public boolean remove(int id) {
    if (!books.containsKey(id)) {
      return false;
    }
    books.remove(id);
    return true;
  }

  @Nullable
  public Book find(int id) {
    return books.get(id);
  }
}
