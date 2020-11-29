package q8_2;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class CallHandler {
  private static CallHandler instance;

  private static final int RANK_LEVELS = 3;
  private static final int NUM_RESPONDENTS = 10;
  private static final int NUM_MANAGERS = 4;
  private static final int NUM_DIRECTORS = 2;

  // employees[0] = responders
  // employees[1] = managers
  // employees[2] = directors
  List<List<Employee>> employees;

  List<List<Call>> callQueues;

  private CallHandler() {
    this.employees = new ArrayList<>(RANK_LEVELS);
    this.callQueues = new ArrayList<>(RANK_LEVELS);

    List<Employee> respondents = new ArrayList<>(NUM_RESPONDENTS);
    IntStream.range(1, NUM_RESPONDENTS).forEach(i -> respondents.add(new Responder()));
    this.employees.set(Rank.Responder.getValue(), respondents);
    this.callQueues.set(Rank.Responder.getValue(), new ArrayList<>());

    List<Employee> managers = new ArrayList<>(NUM_MANAGERS);
    IntStream.range(1, NUM_MANAGERS).forEach(i -> respondents.add(new Manager()));
    this.employees.set(Rank.Manager.getValue(), managers);
    this.callQueues.set(Rank.Manager.getValue(), new ArrayList<>());

    List<Employee> directors = new ArrayList<>(NUM_DIRECTORS);
    IntStream.range(1, NUM_DIRECTORS).forEach(i -> respondents.add(new Director()));
    this.employees.set(Rank.Director.getValue(), directors);
    this.callQueues.set(Rank.Director.getValue(), new ArrayList<>());

  }

  public static CallHandler getInstance() {
    if (instance == null) instance = new CallHandler();
    return instance;
  }

  public void dispatchCall(Call call) {
    Employee emp = getHandlerForCall(call);
    if (emp != null) {
      emp.receiveCall(call);
      call.setHandler(emp);
    } else {
      /* Place the call into corresponding call queue according to its rank. */
      call.reply("Please wait for free employee to reply");
      callQueues.get(call.getRank().getValue()).add(call);
    }
  }

  public boolean assignCall(Employee employee) {
    /* Check the queues, starting from the highest rank this employee can serve. */
    for (int rank = employee.getRank().getValue(); rank >= 0; rank--) {
      List<Call> que = callQueues.get(rank);

      /* Remove the first call, if any */
      if (que.size() > 0) {
        Call call = que.remove(0);
        if (call != null) {
          employee.receiveCall(call);
          return true;
        }
      }
    }
    return false;
  }

  private Employee getHandlerForCall(Call call) {
    for (int level = call.getRank().getValue(); level < RANK_LEVELS - 1; level++) {
      List<Employee> employeeLevel = employees.get(level);
      for (Employee emp : employeeLevel) {
        if (emp.isFree()) {
          return emp;
        }
      }
    }
    return null;
  }
}
