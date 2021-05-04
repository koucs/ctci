package q16_4;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.concurrent.locks.Lock;
import java.util.stream.IntStream;

public class LockFactory {
    private static LockFactory instance;
    private final LockNode[] locks;

    // key: thread owner ID
    // val: そのスレッドがロックすると予告したロックの order
    private final HashMap<Integer, LinkedList<LockNode>> lockOrder;

    private LockFactory(int numberOfNodes) {
        /* default */
        this.locks = new LockNode[numberOfNodes];
        IntStream.range(0, numberOfNodes)
                .forEach(i -> this.locks[i] = new LockNode(i, numberOfNodes));
        this.lockOrder = new HashMap<>();
    }

    public static LockFactory getInstance() {
        return instance;
    }

    public static synchronized LockFactory initialize(int numberOfNodes) {
        if (instance == null) instance = new LockFactory(numberOfNodes);
        return instance;
    }

    public boolean hasCycle(HashMap<Integer, Boolean> touchedNode, int[] resourcesInOrder) {
        for (int resource : resourcesInOrder) {
            if (!touchedNode.get(resource)) {
                LockNode n = this.locks[resource];
                if (n.hasCycle(touchedNode)) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * デッドロックを防ぐため、事前に各スレッドがどのような順番で必要なるかを宣言（予告）させる。
     * サイクル（＝有向グラフ内のサイクル）が発生するかを検出してデッドロック発生を確認する。
     */
    public boolean declare(int ownerId, int[] resourcesInOrder) {
        HashMap<Integer, Boolean> touchedNodes = new HashMap<>();
        // グラフに頂点(Node)を追加
        int index = 1;
        touchedNodes.put(resourcesInOrder[0], false);
        IntStream.range(index, resourcesInOrder.length).forEach(i -> {
            LockNode prev = this.locks[resourcesInOrder[index - 1]];
            LockNode curr = this.locks[resourcesInOrder[index]];
            prev.joinTo(curr);
            touchedNodes.put(resourcesInOrder[index], false);
        });

        // サイクルができてしまった場合はこの resourcesリストを破棄して false を返却
        if (hasCycle(touchedNodes, resourcesInOrder)) {
            for (int j = 1; j < resourcesInOrder.length; j++) {
                LockNode p = this.locks[resourcesInOrder[j - 1]];
                LockNode c = this.locks[resourcesInOrder[j]];
                p.remove(c);
            }
            return false;
        }

        // サイクルが検出されなかった場合は、
        // 実際にスレッドがロックを取得する際に、予告した順番で宣言されていることを確認するための順番を保存する
        LinkedList<LockNode> list = new LinkedList<>();
        for (int j : resourcesInOrder) {
            LockNode resource = this.locks[j];
            list.add(resource);
        }
        this.lockOrder.put(ownerId, list);

        return true;
    }

    public Lock getLock(int ownerId, int resourceID) {
        LinkedList<LockNode> list = lockOrder.get(ownerId);
        if (list == null) {
            return null;
        }

        LockNode head = list.getFirst();
        if (head.getId() == resourceID) {
            list.removeFirst();
            return head.getLock();
        }
        return null;
    }

}
