package q8_5;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class Book {
  private String name;
  private int ID;

  public void print(){
    System.out.printf("ID: %d, name: %s%n", ID, name);
  }

}
