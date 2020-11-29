package q8_2;

public enum Rank {
  Responder(0),
  Manager(1),
  Director(2);
  private final int value;

  Rank(int v) {
    this.value = v;
  }

  public int getValue() {
    return this.value;
  }
}
