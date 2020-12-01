package q8_3;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Builder
@Getter
@Setter
public class Player {
  private PlayList playList;
  private Album album;

  public void playSong() {
    System.out.println("Now Playing ♪ " + playList.getNowPlaying().getName());
    playList.setNowPlaying(playList.getNextSongToPlay());
  }
}
