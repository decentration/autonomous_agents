import unittest
from agents.memory_stream import MemoryStream


class TestMemoryStream(unittest.TestCase):
    def test_add_memory(self):
        memory_stream = MemoryStream()

        memory_data = {
            "id": "unique_id",
            "type": "observation",
            "content": "test_content",
            "importance": 5,
            "timestamp": "2023-01-01T00:00:00Z"
        }

        memory_stream.add_memory(memory_data)

        self.assertEqual(len(memory_stream.nodes), 1)
        self.assertEqual(memory_stream.nodes[0], memory_data)

    def test_get_memory_by_id(self):
        memory_stream = MemoryStream()

        memory_data = {
            "id": "unique_id",
            "type": "observation",
            "content": "test_content",
            "importance": 5,
            "timestamp": "2023-01-01T00:00:00Z"
        }

        memory_stream.add_memory(memory_data)

        retrieved_memory = memory_stream.get_memory_by_id("unique_id")
        self.assertEqual(retrieved_memory, memory_data)

        non_existent_memory = memory_stream.get_memory_by_id("non_existent_id")
        self.assertIsNone(non_existent_memory)
