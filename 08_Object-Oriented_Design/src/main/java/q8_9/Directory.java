package q8_9;

import lombok.Getter;

import java.util.ArrayList;
import java.util.List;

public class Directory extends Entry {
  @Getter protected List<Entry> contents;

  public Directory(String n, Directory p) {
    super(n, p);
    contents = new ArrayList<>();
  }

  public int size() {
    return contents.stream().mapToInt(Entry::size).sum();
  }

  public int numberOfFiles() {
    int directorySizes =
        contents.stream()
            .filter(e -> e instanceof Directory)
            .mapToInt(e -> ((Directory) e).numberOfFiles())
            .sum();
    return contents.size() + directorySizes;
  }

  public void addEntry(Entry entry) {
    contents.add(entry);
  }

  public boolean deleteEntry(Entry entry) {
    return contents.remove(entry);
  }
}
