package q8_5;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class User {
  private int ID;
  private String name;
  private int type;

  public void print(){
    System.out.printf("ID: %d, name: %s, type: %d%n", ID, name, type);
  }
}
