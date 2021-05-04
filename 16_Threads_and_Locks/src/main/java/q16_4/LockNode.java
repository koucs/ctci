package q16_4;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.IntStream;

public class LockNode {
    public enum VisitState {
        FRESH, VISITING, VISITED
    }

    private final int id;
    private final int maxLockNum;
    private Lock lock;
    private final List<LockNode> children;

    public LockNode(int id, int maxLockNum) {
        this.id = id;
        this.maxLockNum = maxLockNum;
        this.children = new ArrayList<>();
    }

    /**
     * サイクルが発生しないことを確認しながら "this" から "node" への辺を追加する
     */
    public void joinTo(LockNode node) {
        children.add(node);
    }

    public void remove(LockNode node) {
        children.remove(node);
    }

    /**
     * 深さ優先探索(DFS)によりサイクルを検出
     */
    public boolean hasCycle(Map<Integer, Boolean> touchedNode) {
        VisitState[] states = new VisitState[maxLockNum];
        IntStream.range(0, maxLockNum).forEach(i -> states[i] = VisitState.FRESH);
        return hasCycle(states, touchedNode);
    }

    private boolean hasCycle(VisitState[] visited, Map<Integer, Boolean> touchedNode) {
        if (touchedNode.containsKey(this.id)) {
            touchedNode.put(this.id, true);
        }
        if (visited[this.id] == VisitState.VISITING) {
            return true;
        } else if (visited[this.id] == VisitState.FRESH) {
            visited[this.id] = VisitState.VISITING;
            for (LockNode c : children) {
                if (c.hasCycle(visited, touchedNode)) return true;
            }
            visited[this.id] = VisitState.VISITED;
        }
        return false;
    }

    public Lock getLock() {
        if (this.lock == null) this.lock = new ReentrantLock();
        return this.lock;
    }

    public int getId() {
        return this.id;
    }
}
