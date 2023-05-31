import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.autonomous_agent import AutonomousAgent


# Create a mock response object
mock_response = Mock()
mock_response.json.return_value = {
    "id": "test_instance_id",
    "type": "test_type",
    "content": "test_content",
    "importance": 1,
    "timestamp": "2023-04-12T12:00:00Z"
}

class TestAutonomousAgent(unittest.TestCase):
    def test_update_memory(self):
        # Define a mock response with a JSON object
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "instance_id": "test_instance_id",
            "other_data": "some_data",
        }

        # Mock the HTTP request
        with patch("requests.get", return_value=mock_response):
            # Mock the MemoryStream class
            with patch("agents.autonomous_agent.MemoryStream") as MockMemoryStream:
                mock_memory_stream = MockMemoryStream.return_value

                # Create an AutonomousAgent instance with a mocked MemoryStream
                # The actual HTTP request will be mocked and return the predefined mock_response
                agent = AutonomousAgent("test_instance_id")
                agent.memory_stream = mock_memory_stream

                # Call the update_memory method
                memory_data = {
                    "id": "unique_id",
                    "type": "observation",
                    "content": "test_content",
                    "importance": 5,
                    "timestamp": "2023-01-01T00:00:00Z"
                }
                agent.update_memory(memory_data)

                # Check if the add_memory method of the mocked MemoryStream was called with the correct argument
                mock_memory_stream.add_memory.assert_called_with(memory_data)

    def test_get_memory(self):
        with patch("requests.get", return_value=mock_response), \
             patch("agents.autonomous_agent.MemoryStream") as MockMemoryStream:

            mock_memory_stream = MockMemoryStream.return_value

            agent = AutonomousAgent("test_instance_id")
            agent.memory_stream = mock_memory_stream

            memory_id = "unique_id"
            agent.get_memory(memory_id)

            mock_memory_stream.get_memory.assert_called_with(memory_id)

    def test_delete_memory(self):
        with patch("requests.get", return_value=mock_response), \
             patch("agents.autonomous_agent.MemoryStream") as MockMemoryStream:

            mock_memory_stream = MockMemoryStream.return_value

            agent = AutonomousAgent("test_instance_id")
            agent.memory_stream = mock_memory_stream

            memory_id = "unique_id"
            agent.delete_memory(memory_id)

            mock_memory_stream.delete_memory.assert_called_with(memory_id)
    
    def test_communicate(self):
        with patch("requests.get", return_value=mock_response), \
             patch("agents.autonomous_agent.MemoryStream") as MockMemoryStream:

            mock_memory_stream = MockMemoryStream.return_value

            agent = AutonomousAgent("test_instance_id")
            agent.memory_stream = mock_memory_stream
            agent.process_message = Mock()

            message_data = {"content": "test message"}

            agent.communicate(message_data)

            agent.process_message.assert_called_with(message_data)

    def test_process_message(self):
        with patch("requests.get", return_value=mock_response), \
             patch("agents.autonomous_agent.MemoryStream") as MockMemoryStream:

            mock_memory_stream = MockMemoryStream.return_value

            agent = AutonomousAgent("test_instance_id")
            agent.memory_stream = mock_memory_stream
            agent.parse_command = Mock(return_value="test_command")
            agent.handle_command = Mock()

            message_data = {"content": "test message"}

            agent.process_message(message_data)

            agent.parse_command.assert_called_with(message_data)
            agent.handle_command.assert_called_with("test_command")