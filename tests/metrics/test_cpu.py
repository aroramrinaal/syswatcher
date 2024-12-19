from src.metrics.cpu import get_cpu_usage

def test_get_cpu_usage():
    usage = get_cpu_usage()
    assert isinstance(usage, float)
    assert 0 <= usage <= 100
