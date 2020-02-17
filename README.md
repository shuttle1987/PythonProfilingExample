# PythonProfilingExample

There's a couple of example snippets of sorting code in `sorting.py` including everyone's favorite bogosort for extra slow (factorial complexity) sorting performance.

## cProfile

You can get a sense of the runtime of Python code with the standard library module cProfile

Try with this:

```bash
python3 -m cProfile slow.py 
```

Compare with:

```bash
python3 -m cProfile fast.py 
```

## Snakeviz

Snakeviz will allow you to see the results of a profiling dump in a nice rendered output.

Do the usual environment stuff then install with:

```bash
pip install snakeviz
```

First create profile output using:

```bash
python3 -m cProfile  -o fast.prof fast.py
```

```bash
python3 -m cProfile  -o slow.prof slow.py
```

Then see the nice visualizaton in your browser using:

```bash
snakeviz slow.prof
```