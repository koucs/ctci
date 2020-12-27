package q8_1;

public abstract class Card {
  public int num;
  public Suit suit;
  public boolean isAvailable = true;

  public Card(int n, Suit s){
    this.num = n;
    this.suit = s;
  }

  public void markAvailable(){
    this.isAvailable = true;
  }
  public void markUnavailable(){
    this.isAvailable = false;
  }

  public void print() {
    System.out.printf("%d - %s%n", this.num, this.suit.name());
  }

}
