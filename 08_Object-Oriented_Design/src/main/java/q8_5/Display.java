package q8_5;

public class Display {
  private User activeUser;
  private Book activeBook;
  private int pageNum;

  public void displayUser(User user) {
    activeUser = user;
    refreshUsername();
  }

  public void displayBook(Book book) {
    activeBook = book;
    pageNum = 0;
    refreshTitle();
    refreshPage();
  }

  public void refreshUsername() {
    /* updates username display */
    activeUser.print();
  }

  public void refreshTitle() {
    /* updates title display */
    activeBook.print();
  }

  public void refreshPage() {
    /* updated page display */
  }

  public void turnPageForward() {
    pageNum++;
    refreshPage();
  }

  public void turnPageBackward() {
    pageNum--;
    refreshPage();
  }

}
