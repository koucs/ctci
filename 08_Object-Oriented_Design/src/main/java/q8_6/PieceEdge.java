package q8_6;

import lombok.Data;

@Data
public class PieceEdge {

  Piece parent;
  EdgeType edgeType;
  int pieceIndex; // Index of Piece.edges[]
  PieceEdge attachedTo; //

  public boolean fitsWith(PieceEdge pieceEdge) {
    // 端同士の連結
    return false;
  }

  public enum EdgeType {
    INNER,
    OUTER,
    FLAT
  }
}
