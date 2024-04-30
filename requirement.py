import os
import sys

import path

bundle_dir = getattr(sys, "_MEIPASS", path.abspath(os.path.dirname(__file__)))
path_to_yml = os.path.abspath(os.path.join(bundle_dir, "config.yml"))
