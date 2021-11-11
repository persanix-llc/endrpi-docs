import os
import subprocess
from shutil import copy

# Build the documentation
subprocess.run(["mkdocs", "build"])

# The build command above wipes the 'out' directory which is where Cloudflare files need to be, copy them in
files = os.listdir(".cloudflare")
for file in files:
    copy(os.path.join(".cloudflare", file), "out")
print("Copied .cloudflare folder contents into out")

