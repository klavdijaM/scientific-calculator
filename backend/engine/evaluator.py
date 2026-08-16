from engine.ast import ASTNode

class Evaluator:
    """Evaluates an abstract syntax tree."""

    def evaluate(self, node: ASTNode) -> float:
        raise NotImplementedError