package q8_4;

import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;

@Getter
@Setter
public abstract class Vehicle {
  protected ArrayList<ParkingSpot> parkingSpots = new ArrayList<>();
  protected String licensePlate;
  protected int spotsNeeded;
  protected VehicleSize size;

  public void parkInSpot(ParkingSpot s) {
    this.parkingSpots.add(s);
  }

  public void clearSpots() {
    parkingSpots.forEach(ParkingSpot::removeVehicle);
    this.parkingSpots.clear();
  }

  public abstract boolean canFitInSpot(ParkingSpot spot);
  public abstract void print();
}
