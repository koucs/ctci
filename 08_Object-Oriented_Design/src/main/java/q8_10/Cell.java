package q8_10;

import lombok.Data;
import lombok.NonNull;

@Data
public class Cell<K, V> {
  @NonNull private K key;
  @NonNull private V value;

  public boolean equivalent(Cell<K, V> c){
    return equals(c.getKey());
  }

  public boolean equivalent(K key1){
    return key.equals(key1);
  }

  @Override
  public String toString() {
    return String.format("{'%s': '%s'}", key, value);
  }
}
