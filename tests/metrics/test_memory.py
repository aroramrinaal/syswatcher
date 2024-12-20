from src.metrics.memory import get_memory_usage

def test_get_memory_usage():
    usage = get_memory_usage()
    # Check if the usage is a float between 0 and 100
    assert isinstance(usage, float)
    assert 0 <= usage <= 100