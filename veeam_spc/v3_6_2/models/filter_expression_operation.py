from enum import Enum


class FilterExpressionOperation(str, Enum):
    AND = "and"
    CONTAINS = "contains"
    EQUALS = "equals"
    EXCLUSIVEOR = "exclusiveOr"
    GREATERTHAN = "greaterThan"
    GREATERTHANOREQUAL = "greaterThanOrEqual"
    IN = "in"
    LESSTHAN = "lessThan"
    LESSTHANOREQUAL = "lessThanOrEqual"
    NOT = "not"
    NOTEQUALS = "notEquals"
    OR = "or"
    SUBSET = "subset"
    SUPERSET = "superset"

    def __str__(self) -> str:
        return str(self.value)
