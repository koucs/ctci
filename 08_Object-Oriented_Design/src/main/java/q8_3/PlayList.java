package q8_3;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.Queue;

@Getter
@Setter
@Builder
public class PlayList {
  private Song nowPlaying;
  private Queue<Song> queue;

  public Song getNextSongToPlay() {
    return this.queue.peek();
  }

  public void addSong(Song song) {
    this.queue.add(song);
  }
}
