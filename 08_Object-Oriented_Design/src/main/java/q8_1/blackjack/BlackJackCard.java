package q8_1.blackjack;

import q8_1.Card;
import q8_1.Suit;

public class BlackJackCard extends Card {

  public BlackJackCard(int n, Suit s) {
    super(n, s);
  }

  public boolean isAce() {
    return this.num == 1;
  }

  public boolean isFaceCard() {
    return 11 <= this.num && this.num <= 13;
  }

  public int value() {
    if (isAce()) return 11;
    else if (isFaceCard()) return 10;
    else return this.num;
  }

  public int max_value() {
    if (isAce()) return 11;
    return this.value();
  }

  public int min_value() {
    if (isAce()) return 1;
    return this.value();
  }
}
