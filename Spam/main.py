import os
import subprocess
import sys
import threading

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


scripts = [
    'bathandbodyworks.py',
    'carolinalemke.py',
    'castro.py',
    'crazyline.py',
    'delta.py',
    'electra.py',
    'footlocker.py',
    'foxhome.py',
    'golbary.py',
    'golfco.py',
    'hamal.py',
    'hoodies.py',
    'housemen.py',
    'intima.py',
    'itay-brands.py',
    'joedelek.py',
    'laline.py',
    'lighting.py',
    'lilitcosmet.py',
    'mishloha.py',
    'naot.py',
    'nautica.py',
    'noizz.py',
    'noyhasade.py',
    'sacara.py',
    'Spices.py',
    'urbanica.py',
    'victoriassecret.py',
    'yvesrocher.py',
    'zygo.py',
]

def run_script(script_name, target_phone): 
    path = os.path.join(_SCRIPT_DIR, script_name)
    if os.path.exists(path):
        try:
            subprocess.run(
                [sys.executable, path, target_phone], 
                check=True,
                cwd=_SCRIPT_DIR,
            )
        except Exception as e:
            print(f"[X] Error: {e}")

def main():
#    target_phone = input("Enter target phone number: ")
    if len(sys.argv) > 1:
    target_phone = sys.argv[1]
else:
    target_phone = input("Enter target phone number: ")
    threads = []
    for script in scripts:
        t = threading.Thread(target=run_script, args=(script, target_phone))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()