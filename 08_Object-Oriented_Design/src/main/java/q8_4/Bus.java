package q8_4;

public class Bus extends Vehicle {

  public Bus() {
    this.spotsNeeded = 4;
    this.size = VehicleSize.Large;
  }

  @Override
  public boolean canFitInSpot(ParkingSpot spot) {
    return spot.getSize() == VehicleSize.Large;
  }

  @Override
  public void print() {
    System.out.print("B");
  }
}
