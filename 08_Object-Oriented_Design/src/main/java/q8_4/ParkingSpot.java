package q8_4;

import lombok.Getter;

@Getter
public class ParkingSpot {
  private Vehicle vehicle;
  private VehicleSize size;
  private int row;
  private int spotNumber;
  private Level level;

  public ParkingSpot(Level lvl, int r, int n, VehicleSize sz) {
    this.level = lvl;
    this.row = r;
    this.spotNumber = n;
    this.size = sz;
  }

  public boolean isAvailable() {
    return this.vehicle == null;
  }

  public boolean canFitVehicle(Vehicle v){
    return isAvailable() && vehicle.canFitInSpot(this);
  }

  public boolean park(Vehicle v){
    if(!canFitVehicle(v)){
      return false;
    }
    this.vehicle = v;
    this.vehicle.parkInSpot(this);
    return true;
  }

  public void removeVehicle() {
    this.vehicle = null;
  }

  public void print() {
    if (this.vehicle == null) {
      if (this.size == VehicleSize.Compact) {
        System.out.print("c");
      } else if (this.size == VehicleSize.Large) {
        System.out.print("l");
      } else if (this.size == VehicleSize.Motorcycle) {
        System.out.print("m");
      }
    } else {
      this.vehicle.print();
    }
  }
}
