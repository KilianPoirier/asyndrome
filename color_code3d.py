import os
from asyndrome import CSSCode

filename = os.path.join(
    os.path.dirname(__file__), "qecc", "manual_color_code_3d_n1.json"
)
code = CSSCode.from_file(filename)
print(code)