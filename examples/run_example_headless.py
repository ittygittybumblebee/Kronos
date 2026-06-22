"""Headless runner for prediction_example.py.

Runs the unmodified example but uses a non-interactive matplotlib backend so the
final plt.show() does not block, saving the figure to a PNG instead. The example
itself is left untouched.
"""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_OUT = os.path.abspath("prediction_output.png")


def _save_instead(*args, **kwargs):
    plt.savefig(_OUT, dpi=120, bbox_inches="tight")
    print("Saved plot to", _OUT)


plt.show = _save_instead

with open("prediction_example.py", encoding="utf-8") as f:
    code = f.read()
exec(compile(code, "prediction_example.py", "exec"), {"__name__": "__main__"})
