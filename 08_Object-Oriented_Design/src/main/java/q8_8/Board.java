package q8_8;

import java.util.HashMap;
import java.util.Map;

public class Board {
  private int blackCount = 0;
  private int whiteCount = 0;
  private Map<Integer, Map<Integer, Piece>> board;

  public Board(int rows, int columns) {
    board = new HashMap<>();
    for (int i = 0; i < rows; i++) {
      Map<Integer, Piece> map = new HashMap<>();
      for (int j = 0; j < columns; j++) {
        map.put(j, null);
      }
      board.put(i, map);
    }
  }

  /** initial board has a grid like the following in the center: WB BW */
  public void initialize() {
    int middleRow = board.size() / 2 - 1;
    int middleColumn = board.get(middleRow).size() / 2 - 1;
    board.get(middleRow).put(middleColumn, new Piece(Color.WHITE));
    board.get(middleRow + 1).put(middleColumn, new Piece(Color.BLACK));
    board.get(middleRow).put(middleColumn + 1, new Piece(Color.BLACK));
    board.get(middleRow + 1).put(middleColumn + 1, new Piece(Color.WHITE));
    blackCount = 2;
    whiteCount = 2;
  }

  public boolean placeColor(int row, int column, Color color) {
    return false;
  }

  private int flipSection(int row, int column, Color color, Direction direction) {
    return 10;
  }

  public int getScore(Color c) {
    return c == Color.BLACK ? blackCount : whiteCount;
  }

  /**
   * The pieceCount number of stones will be added the color's score. (the other color's score will
   * be subtracted)
   *
   * @param newColor color of newly added stones.
   * @param pieceCount number of newly added stones.
   */
  public void updateScore(Color newColor, int pieceCount) {}

  public void print() {
    for (Map.Entry<Integer, Map<Integer, Piece>> entry : this.board.entrySet()) {
      for (Map.Entry<Integer, Piece> child : entry.getValue().entrySet()) {
        if (child.getValue() == null) System.out.print(" _ ");
        else if (child.getValue().getColor() == Color.BLACK) System.out.print(" B ");
        else if (child.getValue().getColor() == Color.WHITE) System.out.print(" W ");
      }
      System.out.println();
    }
  }
}
