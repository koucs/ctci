package q8_3;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.Set;

@Builder
@Setter
@Getter
public class JukeBox {
  private Player player;
  private User user;
  private Set<Album> albums;
}
