import subprocess,os,sys
sys.path.append('../..')
import set_paths

os.chdir("../src")
# os.system("python setup.py -v build_ext")
subprocess.call("python setup.py -v build_ext".split())
