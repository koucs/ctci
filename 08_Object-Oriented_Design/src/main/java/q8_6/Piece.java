package q8_6;

import lombok.Data;

import java.util.List;

@Data
public class Piece {
  List<PieceEdge> pieceEdges;

  public boolean isCorner() {
    return true;
  }
}
