package q8_2;

import java.util.ArrayList;
import java.util.List;

public class Application {
  private static int id = 1;

  public static void main(String[] args) {
    CallHandler ch = CallHandler.getInstance();
    List<Call> calls = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
      Call call = create_call("" + i);
      calls.add(call);
      ch.dispatchCall(call);
      System.out.println(call.getRank());
    }
  }

  private static Call create_call(String name) {
    return new Call(new Caller(id++, name));
  }
}
