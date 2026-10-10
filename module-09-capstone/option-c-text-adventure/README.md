# Option C: Text adventure

A small game with at least 4 rooms, items you can pick up, one locked door and a way
to win. It saves and loads progress. The starter has 3 rooms, so add a fourth.

Build order: the world as a dictionary, player state in one dictionary, a pure
`parse_command()` you can test, one function per verb, then save/load with JSON.

```text
cd starter
pip install pytest
pytest
python game.py
```
