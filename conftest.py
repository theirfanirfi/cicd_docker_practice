"""Makes the project root importable so tests can `from app import app`.

pytest prepends the directory containing the rootdir conftest.py to sys.path,
which keeps `pytest` and `python -m pytest` behaving the same.
"""
