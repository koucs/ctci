package q8_4;

import java.util.List;

public class ParkingLot {
  private List<Level> levels;
  private final int NUM_LEVELS;

  public ParkingLot(List<Level> levels) {
    this.levels = levels;
    this.NUM_LEVELS = levels.size();
  }

  public boolean parkVehicle(Vehicle v) {
    for (Level level : this.levels) {
      if (level.parkVehicle(v)) {
        return true;
      }
    }
    return false;
  }

  public void print() {
    for (int i = 0; i < levels.size(); i++) {
      System.out.print("Level" + i + ": ");
      levels.get(i).print();
      System.out.println();
    }
    System.out.println();
  }
}
