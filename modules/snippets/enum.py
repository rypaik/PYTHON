from enum import Enum


class DayOfWeek(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


x = DayOfWeek.MONDAY
y = DayOfWeek.FRIDAY

print(DayOfWeek.FRIDAY)
print(DayOfWeek.FRIDAY.name)
print(DayOfWeek.MONDAY.value)


x = DayOfWeek("monday")
print(x)

for day in DayOfWeek:
    print(day)







#### AUTO FUNCTION FOR ENUM

from enum import Enum, auto

class DayOfWeek(Enum):
  MONDAY = auto()
  TUESDAY = auto()
  WEDNESDAY = auto()
  THURSDAY = auto()
  FRIDAY = auto()
  SATURDAY = auto()
  SUNDAY = auto()



#### IntEnum Class
from enum import IntEnumclass DayOfWeek(IntEnum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7


print(DayOfWeek.WEDNESDAY > DayOfWeek.MONDAY)
print(DayOfWeek.WEDNESDAY == 3)


# https://docs.python.org/3/library/enum.html
# https://www.geeksforgeeks.org/enum-in-python/
