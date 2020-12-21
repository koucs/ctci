package q8_8;

import lombok.Getter;

public class Piece {
  @Getter private Color color;

  public Piece(Color c) {
    color = c;
  }

  public void flip() {
    color = color == Color.BLACK ? Color.WHITE : Color.BLACK;
  }
}
