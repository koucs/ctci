package q8_2;

public class Employee {
  protected Rank rank;
  private Call call = null;

  public Employee() {}

  public void receiveCall(Call call) {
    this.call = call;
  }

  public void callCompleted() {
    if (this.call != null) {
      this.call.disconnect();
      this.call = null;
    }
    assignNewCall();
  }

  public void escalateAndReassign() {
    if (this.call != null) {
      /* escalate call */
      this.call.incrementRank();
      CallHandler.getInstance().dispatchCall(this.call);

      /* free the employee */
      this.call = null;
    }

    /* assign a new call */
    assignNewCall();
  }

  /* Assign a new call to an employee, if the employee is free. */
  public boolean assignNewCall() {
    if (!isFree()) {
      return false;
    }
    return CallHandler.getInstance().assignCall(this);
  }

  /* Returns whether or not the employee is free. */
  public boolean isFree() {
    return this.call == null;
  }

  public Rank getRank() {
    return this.rank;
  }
}
