NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
"""[a:b:c]
a = Start
b = Stop
c = Step
(if Step is negative, reverse order by n steps)"""
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
