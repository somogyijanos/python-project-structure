# Structuring a Python Project
This is a simple and clean example how to structure a Python project such that (absolute/relative) imports don't get messed up.

## Requirements
- Python 3

## Usage
There are three python files included in this example. The idea is that all of them can be run individually and the imports still work **if run from the project root**:

```bash
python main.py
python app/addition.py
python app/conversion.py
```
Alternatively you can also just run:
```bash
bash run.sh
```

## Acknowledgements
Inspired by [this](https://stackoverflow.com/a/16985066) answer on stack overflow.