package q8_4;

import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Application {
  public static void main(String[] args) {
    List<Level> levels =
        IntStream.range(0, 5).boxed().map(i -> new Level(i, 30)).collect(Collectors.toList());

    ParkingLot lot = new ParkingLot(levels);

    Vehicle v = null;
    Random random = new Random();
    while (v == null || lot.parkVehicle(v)) {
      lot.print();
      int r = random.nextInt(10);
      if (r < 2) {
        v = new Bus();
      } else if (r < 4) {
        v = new Motorcycle();
      } else {
        v = new Car();
      }
      System.out.print("\nParking a ");
      v.print();
      System.out.println();
    }
    System.out.println("Parking Failed. Final state: ");
    lot.print();
  }
}
