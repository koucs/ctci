package q8_5;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class OnlineReaderSystem {
  private BookLibrary bookLibrary;
  private UserManager userManager;
  private Display display;

  private Book activeBook;
  private User activeUser;

  public OnlineReaderSystem(){
    userManager = new UserManager();
    bookLibrary = new BookLibrary();
    display = new Display();
  }

  public void setActiveBook(Book book) {
    display.displayBook(book);
    activeBook = book;
  }

  public void setActiveUser(User user) {
    activeUser = user;
    display.displayUser(user);
  }
}
