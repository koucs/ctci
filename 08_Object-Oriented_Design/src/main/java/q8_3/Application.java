package q8_3;

import com.google.common.collect.ImmutableMap;
import com.google.common.collect.Queues;

import java.util.*;

public class Application {
  public static void main(String[] args) {
    User u = User.builder().id("1").name("xeon").build();

    Map<String, Integer> map = ImmutableMap.of("FLAME VEIN", 8, "THE LIVING DEAD", 11, "orbital period", 16);

    Queue<Album> albums = Queues.newArrayDeque();
    map.forEach((key, value) -> {
      List<Song> songs = new ArrayList<>();
      for (int j = 1; j <= value; j++) {
        songs.add(Song.builder().name(key + " - Track " + j).build());
      }
      albums.add(Album.builder().collections(songs).build());
    });

    Album album = Optional.ofNullable(albums.poll()).orElse(Album.builder().build());
    Queue<Song> songs = Queues.newArrayDeque(album.getCollections());
    Player player = Player.builder()
            .album(albums.poll())
            .playList(PlayList.builder().nowPlaying(songs.peek()).queue(songs).build())
            .build();
    JukeBox jukeBox = JukeBox.builder()
            .albums(new HashSet<>(albums))
            .player(player)
            .user(u)
            .build();

    jukeBox.getPlayer().playSong();

  }
}
