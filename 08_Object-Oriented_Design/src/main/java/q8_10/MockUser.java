package q8_10;

import lombok.Data;
import lombok.NonNull;

@Data
public class MockUser {
  @NonNull private Integer age;
  @NonNull private String name;

  @Override
  public String toString() {
    return String.format("Age: %d, Name: %s", age, name);
  }
}
