package q8_10;

import java.util.LinkedList;

public class Hash<K, V> {
  private LinkedList<Cell<K, V>>[] items;

  public Hash() {
    items = (LinkedList<Cell<K, V>>[]) new LinkedList[400];
  }

  public int hashCodeOfKey(K key) {
    return key.toString().length() % items.length;
  }

  public void put(K key, V value) {
    int h = hashCodeOfKey(key);
    if (items[h] == null) {
      items[h] = new LinkedList<>();
    }
    LinkedList<Cell<K, V>> cells = items[h];
    for (Cell<K, V> cell : cells) {
      if (cell.equivalent(key)) {
        cells.remove(cell);
        break;
      }
    }
    cells.add(new Cell<>(key, value));
  }

  public V get(K key) {
    int h = hashCodeOfKey(key);
    if (items[h] == null) {
      return null;
    }
    LinkedList<Cell<K, V>> cells = items[h];
    for (Cell<K, V> cell : cells) {
      if (cell.equivalent(key)) return cell.getValue();
    }
    return null;
  }

  public void debugPrint() {
    for (int i = 0; i < items.length; i++) {
      if (items[i] == null) continue;
      System.out.print(i + ": ");
      items[i].forEach(c -> System.out.print(c.getKey() + ": " + c.getValue() + ", "));
      System.out.println();
    }
  }
}
