package q8_9;

import lombok.Getter;
import lombok.Setter;

public class File extends Entry {
  @Getter @Setter
  private String content;
  private int size;

  public File(String n, Directory p, String c) {
    super(n, p);
    content = c;
    size = c.length();
  }

  public int size() {
    return size;
  }
}
