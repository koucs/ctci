package q8_8;

import java.util.Arrays;

import static q8_8.Direction.UP;
import static q8_8.Direction.DOWN;
import static q8_8.Direction.LEFT;
import static q8_8.Direction.RIGHT;

public class Board {
  private int blackCount = 0;
  private int whiteCount = 0;
  private Piece[][] board;

  public Board(int rows, int columns) {
    board = new Piece[rows][columns];
  }

  /** initial board has a grid like the following in the center: WB BW */
  public void initialize() {
    int middleRow = board.length / 2 - 1;
    int middleColumn = board[middleRow].length / 2 - 1;
    board[middleRow][middleColumn] = new Piece(Color.WHITE);
    board[middleRow + 1][middleColumn] = new Piece(Color.BLACK);
    board[middleRow][middleColumn + 1] = new Piece(Color.BLACK);
    board[middleRow + 1][middleColumn + 1] = new Piece(Color.WHITE);

    blackCount = 2;
    whiteCount = 2;
  }

  public boolean placeColor(int row, int column, Color color) {
    if (board[row][column] != null) {
      return false;
    }

    int[] results = new int[4];
    results[0] = flipSection(row - 1, column, color, UP);
    results[1] = flipSection(row + 1, column, color, DOWN);
    results[2] = flipSection(row, column - 1, color, LEFT);
    results[3] = flipSection(row, column + 1, color, RIGHT);

    int flipped = Arrays.stream(results).filter(i -> i > 0).sum();

    // To check an invalid move
    if (flipped < 0) {
      return false;
    }

    board[row][column] = new Piece(color);
    updateScore(color, flipped + 1);

    return true;
  }

  /**
   * @return int (-1 is error)
   */
  private int flipSection(int row, int column, Color color, Direction direction) {
    int dr = 0, dc = 0;
    if (direction == UP) dr = -1;
    else if (direction == DOWN) dr = 1;
    else if (direction == LEFT) dc = -1;
    else dc = 1;

    if (row < 0
        || board.length <= row
        || column < 0
        || board[row].length <= column
        || board[row][column] == null) {
      return -1;
    }

    if (board[row][column].getColor() == color) return 0;

    int flipped = flipSection(row + dr, column + dc, color, direction);
    if (flipped < 0) return -1;

    board[row][column].flip();
    return flipped + 1;
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
  public void updateScore(Color newColor, int pieceCount) {
    if (newColor == Color.BLACK) {
      this.whiteCount -= pieceCount - 1;
      this.blackCount += pieceCount;
    } else {
      this.whiteCount += pieceCount;
      this.blackCount -= pieceCount - 1;
    }
  }

  public void print() {
    for (Piece[] parent : this.board) {
      for (Piece child : parent) {
        if (child == null) System.out.print(" _ ");
        else if (child.getColor() == Color.BLACK) System.out.print(" B ");
        else if (child.getColor() == Color.WHITE) System.out.print(" W ");
      }
      System.out.println();
    }
  }
}
