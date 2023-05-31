
from memory import Observation, Plan, Ideal, Reflection

def test_memory_number_increment():
    # Create some memory items
    memory1 = Observation("Observation 1", "2023-04-17 12:00:00", 5)
    memory2 = Plan("Plan 1", "2023-04-17 13:00:00", 6)
    memory3 = Ideal("Ideal 1", "2023-04-17 14:00:00", 7)
    memory4 = Reflection("Reflection 1", 8, "2023-04-17 15:00:00", [])


    # Check if memory numbers are incremented
    assert memory1.number == 0, f"Memory 1 number expected 0, got {memory1.number}"
    assert memory2.number == 1, f"Memory 2 number expected 1, got {memory2.number}"
    assert memory3.number == 2, f"Memory 3 number expected 2, got {memory3.number}"
    assert memory4.number == 3, f"Memory 4 number expected 3, got {memory4.number}"



test_memory_number_increment()
