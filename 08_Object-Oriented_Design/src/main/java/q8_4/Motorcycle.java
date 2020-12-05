package q8_4;

public class Motorcycle extends Vehicle{

  public Motorcycle(){
    this.spotsNeeded = 1;
    this.size = VehicleSize.Motorcycle;
  }

  @Override
  public boolean canFitInSpot(ParkingSpot spot) {
    // Motorcycle will fit any size of ParkingSpot.
    return true;
  }

  @Override
  public void print() {
    System.out.print("M");
  }
}
