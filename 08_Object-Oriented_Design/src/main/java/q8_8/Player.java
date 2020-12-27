package q8_8;

import lombok.Data;

@Data
public class Player {
  private Color color;

  public Player(Color c) {
    color = c;
  }

  public int getScore(){
    return Game.getInstance().getBoard().getScore(this.color);
  }

  public boolean placePiece(int row, int column) {
    return Game.getInstance().getBoard().placeColor(row, column, this.color);
  }
}
