package q8_8;

public class Application {
  public static void main(String[] args) {
    Game game = Game.getInstance();
    game.getBoard().initialize();

    print();

    System.out.println("WHITE RECOMMEND");
    game.getBoard().print_recommend(Color.WHITE);
    System.out.println("BLACK RECOMMEND");
    game.getBoard().print_recommend(Color.BLACK);

    System.out.println();
    game.getBoard().placeColor(3, 4, Color.BLACK);

    print();
  }

  public static void print() {
    Game game = Game.getInstance();
    System.out.printf(
        "W: %d vs %d :B \n",
        game.getBoard().getScore(Color.WHITE), game.getBoard().getScore(Color.BLACK));
    game.getBoard().print();
    System.out.println();
  }
}
