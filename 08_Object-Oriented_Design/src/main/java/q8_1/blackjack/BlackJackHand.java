package q8_1.blackjack;

import q8_1.Card;
import q8_1.Hand;

import java.util.ArrayList;
import java.util.List;

public class BlackJackHand extends Hand<BlackJackCard> {
  @Override
  public int score() {
    int score = 0;
    for (BlackJackCard card : this.cards) {
      score += card.value();
    }
    return score;
  }

  public List<Integer> scoreList() {
    List<Integer> scoreList = new ArrayList<>();

    if (this.cards.size() == 0) {
      return scoreList;
    }

    for (BlackJackCard card : this.cards) {
      if (scoreList.size() == 0) {
        scoreList.add(0);
      }
      int size = scoreList.size();
      for (int i = 0; i < size; i++) {
        scoreList.set(i, scoreList.get(i) + card.min_value());
        if (card.min_value() != card.max_value()) {
          scoreList.set(i, scoreList.get(i) + card.max_value());
        }
      }
    }

    return scoreList;
  }

  public boolean busted(){
    return this.score() > 21;
  }


  public boolean isBlackJack(){
    if (this.cards.size() != 2){
      return false;
    }
    BlackJackCard first = cards.get(0);
    BlackJackCard second = cards.get(1);
    return (first.isAce() && second.isFaceCard())
            || (first.isFaceCard() && second.isAce());
  }

}
