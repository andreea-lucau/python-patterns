"""Sample usage of the Interpreter pattern.

Define a grammar for a simple calculator and evaluate an expression.
"""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

import yaml

def add(left_term, right_term):
    return left_term + right_term


def sub(left_term, right_term):
    return left_term - right_term


class Expression(object):
    def __init__(self, input_operations):
        self.operation = {}
        self.value = None

        if hasattr(input_operations, "items"):
            for operator, terms in input_operations.items():
                self.add_operation(operator, terms)
        else:
            self.value = input_operations

    def add_operation(self, operator, terms):
        self.operation = {
            "operator": operator,
            "terms": [
                Expression(term) for term in terms
            ],
        }

    def evaluate(self):
        if self.operation:
            result = self.operation["terms"][0].evaluate()
            for term in self.operation["terms"][1:]:
                result = globals()[self.operation["operator"]](
                    result, term.evaluate()
                )
            return result
        else:
            return self.value

    def __repr__(self):
        if self.operation:
            return "(" + ("  " + self.operation["operator"] + "  ").join([
                str(term) for term in self.operation["terms"]
            ]) + ")"
        else:
            return str(self.value)


def calculate():
    with open("operations.yaml") as ops:
        operations = yaml.load(ops)
    expr = Expression(operations)

    print "Expression:", expr
    print "Evaluated expression: ", expr.evaluate()


if __name__ == "__main__":
    calculate()
