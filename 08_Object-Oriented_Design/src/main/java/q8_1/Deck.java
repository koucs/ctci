package q8_1;

import java.util.ArrayList;
import java.util.List;

public class Deck<T extends Card> {
  private List<T> cards;
  // marks first undealt card
  private int firstUnDealIndex = 0;

  public void shuffle() {}

  public void setCards(List<T> cards) {
    this.cards = cards;
  }

  public int remainingCardsNum() {
    return this.cards.size() - this.firstUnDealIndex;
  }

  public List<T> dealHand(int num) {
    if (remainingCardsNum() < num) {
      return null;
    }

    ArrayList<T> hand = new ArrayList<T>();

    for (int i = 0; i < num; i++) {
      T card = this.dealCard();
      hand.add(card);
    }

    return hand;
  }

  public T dealCard() {
    if (remainingCardsNum() == 0) {
      return null;
    }
    T card = this.cards.get(this.firstUnDealIndex);
    card.markUnavailable();
    this.firstUnDealIndex++;
    return card;
  }
}
