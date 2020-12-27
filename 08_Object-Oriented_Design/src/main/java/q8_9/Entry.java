package q8_9;

import lombok.Getter;

@Getter
public abstract class Entry {
  protected Directory parent;
  protected long created;
  protected long lastUpdated;
  protected long lastAddressed;
  protected String name;

  public Entry(String n, Directory p) {
    name = n;
    parent = p;
    created = System.currentTimeMillis();
    lastUpdated = System.currentTimeMillis();
    lastAddressed = System.currentTimeMillis();
  }

  public abstract int size();

  public boolean delete() {
    if (parent == null) return false;
    return parent.delete();
  }

  public String getFullPath() {
    if (parent == null) return name;
    return parent.getFullPath() + "/" + name;
  }

  public void changeName(String n) {
    name = n;
  }
}
