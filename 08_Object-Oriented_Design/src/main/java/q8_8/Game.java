package q8_8;

import com.google.common.collect.ImmutableList;
import lombok.Getter;

import java.util.List;

public class Game {
  private static Game instance;
  @Getter private Board board;
  private List<Player> players;
  private final int ROW = 10;
  private final int COLUMN = 10;

  private Game() {
    this.board = new Board(ROW, COLUMN);
    this.players = ImmutableList.of(new Player(Color.WHITE), new Player(Color.BLACK));
  }

  public static Game getInstance() {
    if (instance == null) {
      instance = new Game();
    }
    return instance;
  }
}
