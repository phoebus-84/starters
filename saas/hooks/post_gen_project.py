import os
import sys
import shutil

def create_env():
    print("Creating .env file...")
    base_dir = os.path.join(os.getcwd(), "webapp")
    source_file = os.path.join(base_dir, '.env.example')
    destination_file = os.path.join(base_dir, '.env')
    shutil.copyfile(source_file, destination_file)

if __name__ == '__main__':
    sys.exit(create_env())
    
