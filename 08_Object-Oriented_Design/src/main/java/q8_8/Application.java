package q8_8;

public class Application {
  public static void main(String[] args) {
    Game game = Game.getInstance();
    game.getBoard().initialize();
    game.getBoard().print();
  }
}
