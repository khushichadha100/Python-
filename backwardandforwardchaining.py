class Rule:
    def __init__(self, conclusion, premises):
        self.conclusion = conclusion
        self.premises = premises

class Fact:
    def __init__(self, predicate, terms):
        self.predicate = predicate
        self.terms = terms

class KnowledgeBase:
    def __init__(self):
        self.rules = []
        self.facts = []
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    def add_fact(self, fact):
        self.facts.append(fact)

    def backward_chaining(self, goal):
        visited = set()

        def bc_ask(predicate):
            if predicate in visited:
                return False
            visited.add(predicate)

            for fact in self.facts:
                if fact.predicate == predicate:
                    return True

            for rule in self.rules:
                if rule.conclusion.predicate == predicate:
                    all_premises_true = all(bc_ask(premise.predicate) for premise in rule.premises)
                    if all_premises_true:
                        return True

            return False

        return bc_ask(goal)

    def forward_chaining(self, goal):
        inferred_facts = set()
        agenda = []

        for fact in self.facts:
            agenda.append(fact)

        while agenda:
            current_fact = agenda.pop(0)
            inferred_facts.add(current_fact.predicate)

            if current_fact.predicate == goal:
                return True

            for rule in self.rules:
                if rule.conclusion.predicate == current_fact.predicate:
                    new_fact = Fact(rule.conclusion.predicate, rule.conclusion.terms)
                    if new_fact.predicate not in inferred_facts:
                        agenda.append(new_fact)

        return False

# Creating a Knowledge Base
kb = KnowledgeBase()

# Adding rules
rule1 = Rule(Fact("parent", ["alice", "bob"]), [Fact("mother", ["alice", "bob"])])
rule2 = Rule(Fact("parent", ["alice", "charlie"]), [Fact("mother", ["alice", "charlie"])])
rule3 = Rule(Fact("parent", ["alice", "david"]), [Fact("mother", ["alice", "david"])])
kb.add_rule(rule1)
kb.add_rule(rule2)
kb.add_rule(rule3)

# Adding facts
fact1 = Fact("mother", ["alice", "bob"])
fact2 = Fact("mother", ["alice", "charlie"])
kb.add_fact(fact1)
kb.add_fact(fact2)

# Querying with Backward Chaining
print("Backward Chaining:")
print("Is 'bob' a child of 'alice'?")
result_bc = kb.backward_chaining("parent(['alice', 'bob'])")
print("Result:", result_bc)

# Querying with Forward Chaining
print("\nForward Chaining:")
print("Is 'david' a child of 'alice'?")
result_fc = kb.forward_chaining("parent(['alice', 'david'])")
print("Result:", result_fc)
