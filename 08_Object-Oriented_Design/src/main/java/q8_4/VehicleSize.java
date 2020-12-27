package q8_4;

public enum VehicleSize {
  Motorcycle(0),
  Compact(1),
  Large(2);

  private int value;

  VehicleSize(int v) {
    this.value = v;
  }

  public static VehicleSize getVehicleSizeFromValue(int value){
    if (value == 0){
      return VehicleSize.Motorcycle;
    } else if(value == 1){
      return VehicleSize.Compact;
    } else {
      return VehicleSize.Large;
    }
  }
}
