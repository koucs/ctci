package q8_10;

import com.google.common.collect.ImmutableList;

import java.util.List;

public class Application {
  public static void main(String[] args) {
    List<MockUser> users =
        ImmutableList.of(
            new MockUser(12, "alice"),
            new MockUser(18, "bob"),
            new MockUser(24, "carry"),
            new MockUser(30, "david"),
            new MockUser(30, "elza"),
            new MockUser(30, "fife"),
            new MockUser(30, "gonzales"),
            new MockUser(130, "bob"));
    Hash<String, MockUser> hash = new Hash<>();
    for (MockUser user : users) {
      hash.put(user.getName(), user);
    }
    hash.debugPrint();

    for (MockUser user : users) {
      System.out.printf(
          "name: %s, result: %s \n",
          user.toString(), hash.get(user.getName()) == user ? "Exist" : "Not Exist");
    }
  }
}
