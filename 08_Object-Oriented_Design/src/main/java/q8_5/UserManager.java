package q8_5;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import java.util.HashMap;

public class UserManager {
  private final HashMap<Integer, User> users = new HashMap<>();

  @Nullable
  public User addUser(int id, @Nonnull String name, int type) {
    if (users.containsKey(id)) {
      return null;
    }
    User u = User.builder().ID(id).name(name).type(type).build();
    users.put(id, u);
    return u;
  }

  public boolean remove(User user) {
    return remove(user.getID());
  }

  public boolean remove(int id) {
    if (!users.containsKey(id)) {
      return false;
    }
    users.remove(id);
    return true;
  }

  @Nullable
  public User find(int id) {
    return users.get(id);
  }
}
