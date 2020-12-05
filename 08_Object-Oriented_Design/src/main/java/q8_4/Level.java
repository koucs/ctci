package q8_4;

import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Getter
@Setter
public class Level {
  private int floor;
  private List<ParkingSpot> spots;
  private int availableSpots;
  private static final int SPOTS_PER_LOW = 10;

  public Level(int floor, int numberSpots) {
    this.floor = floor;
    this.spots = new ArrayList<>();
    int largeSpots = numberSpots / 4;
    int compactSpots = numberSpots / 4;
    int motorCycleSpots = numberSpots - largeSpots - compactSpots;

    IntStream.rangeClosed(0, largeSpots)
        .boxed()
        .collect(Collectors.toList())
        .forEach(i -> spots.add(new ParkingSpot(this, i / SPOTS_PER_LOW, i, VehicleSize.Large)));
    IntStream.rangeClosed(largeSpots, largeSpots + largeSpots)
        .boxed()
        .collect(Collectors.toList())
        .forEach(i -> spots.add(new ParkingSpot(this, i / SPOTS_PER_LOW, i, VehicleSize.Compact)));
    IntStream.rangeClosed(compactSpots + largeSpots, numberSpots)
        .boxed()
        .collect(Collectors.toList())
        .forEach(
            i -> spots.add(new ParkingSpot(this, i / SPOTS_PER_LOW, i, VehicleSize.Motorcycle)));

    this.availableSpots = numberSpots;
  }

  public boolean parkVehicle(Vehicle vehicle) {
    if (this.availableSpots < vehicle.getSpotsNeeded()) {
      return false;
    }
    int spotNumber = findAvailableSpots(vehicle);
    if (spotNumber < 0) {
      return false;
    }
    return parkStartingAtSpot(spotNumber, vehicle);
  }

  private boolean parkStartingAtSpot(int spotNumber, Vehicle vehicle) {
    vehicle.clearSpots();
    boolean success = true;
    for (int i = spotNumber; i < spotNumber + vehicle.spotsNeeded; i++) {
      success &= spots.get(i).park(vehicle);
    }
    availableSpots -= vehicle.spotsNeeded;
    return success;
  }

  /* find a spot to park this vehicle. Return index of spot, or -1 on failure. */
  private int findAvailableSpots(Vehicle vehicle) {
    int spotsNeeded = vehicle.getSpotsNeeded();
    int lastRow = -1;
    int spotsFound = 0;
    for (int i = 0; i < spots.size(); i++) {
      ParkingSpot spot = spots.get(i);
      if (lastRow != spot.getRow()) {
        spotsFound = 0;
        lastRow = spot.getRow();
      }
      if (spot.canFitVehicle(vehicle)) {
        spotsFound++;
      } else {
        spotsFound = 0;
      }
      if (spotsFound == spotsNeeded) {
        return i - (spotsNeeded - 1);
      }
    }
    return -1;
  }

  public void print() {
    int lastRow = -1;
    for (ParkingSpot spot : spots) {
      if (spot.getRow() != lastRow) {
        System.out.print("  ");
        lastRow = spot.getRow();
      }
      spot.print();
    }
  }

  /* When a car was removed from the spot, increment availableSpots */
  public void spotFreed() {
    availableSpots++;
  }
}
