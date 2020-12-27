package q8_4;

public class Car extends Vehicle {

  public Car() {
    this.spotsNeeded = 1;
    this.size = VehicleSize.Compact;
  }

  @Override
  public boolean canFitInSpot(ParkingSpot spot) {
    return spot.getSize() == VehicleSize.Compact || spot.getSize() == VehicleSize.Large;
  }

  @Override
  public void print() {
    System.out.print("C");
  }
}
