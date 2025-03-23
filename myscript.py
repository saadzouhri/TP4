import os
import sys


bad_hash = sys.argv[1]  
good_hash = sys.argv[2]  

os.system(f"git bisect start {bad_hash} {good_hash}")

exit_code = os.system("git bisect run python manage.py test")

os.system("git bisect reset")

sys.exit(exit_code)
