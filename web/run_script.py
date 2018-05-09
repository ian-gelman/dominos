
import json
import subprocess

def run_script():
    data = json.load(open('store.json', 'r'))
    script = data['script_to_run']

    subprocess.call(['/usr/bin/python', script])
    
    return 0



if __name__ == "__main__":
    run_script()