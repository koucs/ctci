package q8_8;

import lombok.Data;

@Data
public class Location {
  private int row;
  private int column;

  public boolean isSameAs(int r, int c) {
    return this.row == r && this.column == c;
  }
}
