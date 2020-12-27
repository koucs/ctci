package q8_1;

public enum Suit {
  SPADES(0),
  HEARTS(1),
  DIAMONDS(2),
  CLUBS(3);

  private int value;

  Suit(int v) {
    value = v;
  }

  public int getValue() {
    return value;
  }

  public static Suit getSuitFromValue(int value) {
    if (value == 0) {
      return Suit.SPADES;
    } else if (value == 1) {
      return Suit.HEARTS;
    } else if (value == 2) {
      return Suit.DIAMONDS;
    } else {
      return Suit.CLUBS;
    }
  }
}
