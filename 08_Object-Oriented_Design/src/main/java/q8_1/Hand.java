package q8_1;

import java.util.ArrayList;
import java.util.List;

public class Hand<T extends Card> {
  protected List<T> cards = new ArrayList<>();

  public int score() {
    int score = 0;
    for (T card : this.cards) {
      score += card.num;
    }
    return score;
  }

  public void addCard(T card) {
    this.cards.add(card);
  }

  public void print() {
    for (Card card : cards) {
      card.print();
    }
  }
}
