package q8_6;

import com.google.common.collect.Table;

import static q8_6.PieceEdge.EdgeType.FLAT;
import static q8_6.PieceEdge.EdgeType.INNER;
import static q8_6.PieceEdge.EdgeType.OUTER;

import java.util.List;

/** 前提条件: - Pieceに向きは変更不要 */
public class Puzzle {
  // 未配置のピース
  List<Piece> pieces;

  Table<Integer, Integer, Piece> solution;

  List<Piece> corners;

  List<PieceEdge> inners, outers, flats;

  void sort() {
    for (Piece p : pieces) {
      if (p.isCorner()) corners.add(p);
      for (PieceEdge e : p.pieceEdges) {
        if (e.edgeType == INNER) inners.add(e);
        else if (e.edgeType == OUTER) outers.add(e);
      }
    }
  }

  void solve() {
    PieceEdge currentEdge = getExposedEdge(corners.get(0));

    while (currentEdge != null) {
      List<PieceEdge> oppositeEdges = currentEdge.edgeType == INNER ? outers : inners;
      for (PieceEdge fittingEdge : oppositeEdges) {
        if (currentEdge.fitsWith(fittingEdge)) {
          attachEdges(currentEdge, fittingEdge);
          removeFromList(fittingEdge);
          removeFromList(currentEdge);

          currentEdge = nextExposedEdge(fittingEdge);
          break;
        }
      }
    }
  }

  public void removeFromList(PieceEdge e) {
    if (e.edgeType == INNER) {
      inners.remove(e);
    } else if (e.edgeType == OUTER) {
      inners.remove(e);
    }
  }

  public PieceEdge nextExposedEdge(PieceEdge edge) {
    int next_index = (edge.pieceIndex + 2) % 4;
    PieceEdge next_edge = edge.parent.pieceEdges.get(next_index);
    if (isExposed(next_edge)) {
      return next_edge;
    }
    return getExposedEdge(edge.parent);
  }

  public void attachEdges(PieceEdge e1, PieceEdge e2) {
    e1.attachedTo = e2;
    e2.attachedTo = e1;
  }

  public boolean isExposed(PieceEdge edge) {
    return edge.edgeType != FLAT && edge.attachedTo == null;
  }

  public PieceEdge getExposedEdge(Piece p) {
    for (PieceEdge edge : p.pieceEdges) {
      if (isExposed(edge)) {
        return edge;
      }
    }
    return null;
  }
}
