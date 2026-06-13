from typing import Protocol


class FraudScoringStrategy(Protocol):
    def score(self, transaction: dict) -> float:
        ...


class RuleBasedFraudScoring:
    def score(self, transaction: dict) -> float:
        amount = transaction["amount"]
        country = transaction["country"]

        score = 0.0

        if amount > 100000:
            score += 0.5

        if country not in {"IN", "US", "UK"}:
            score += 0.3

        return min(score, 1.0)


class MLBasedFraudScoring:
    def score(self, transaction: dict) -> float:
        # In real system, this would call an ML model.
        return 0.72


class HybridFraudScoring:
    def __init__(
        self,
        rule_strategy: FraudScoringStrategy,
        ml_strategy: FraudScoringStrategy,
    ):
        self.rule_strategy = rule_strategy
        self.ml_strategy = ml_strategy

    def score(self, transaction: dict) -> float:
        rule_score = self.rule_strategy.score(transaction)
        ml_score = self.ml_strategy.score(transaction)

        return round((rule_score * 0.4) + (ml_score * 0.6), 2)


class FraudDetectionService:
    def __init__(self, scoring_strategy: FraudScoringStrategy):
        self.scoring_strategy = scoring_strategy

    def evaluate(self, transaction: dict) -> dict:
        fraud_score = self.scoring_strategy.score(transaction)

        return {
            "fraud_score": fraud_score,
            "decision": "BLOCK" if fraud_score >= 0.75 else "ALLOW"
        }


transaction = {
    "amount": 150000,
    "country": "IN",
    "user_id": "U101"
}


obj1 = FraudDetectionService(RuleBasedFraudScoring())
print(obj1.evaluate(transaction))


"""
strategy = HybridFraudScoring(
    rule_strategy=RuleBasedFraudScoring(),
    ml_strategy=MLBasedFraudScoring(),
)

service = FraudDetectionService(strategy)

print(service.evaluate(transaction))"""