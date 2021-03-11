from subprocess import Popen, PIPE, STDOUT
import os.path
import pathlib

REPORTS_DIRECTORY = 'reports'
ARGUMENT_FILE_NAME = 'arguments.txt'

path_to_argument_file = ''
tests_path = ''

def run_tests():
    """
    Runs the robot framework tests.
    """
    create_argument_file()
    run_robot()

def run_robot():
    """
    Runs the robot framework subprocess.
    """

    suites_path = os.path.join(tests_path, 'suites')
    print(tests_path)
    command = ['robot', suites_path, '--argumentfile', path_to_argument_file]
    process = Popen(command, stdout=PIPE, stderr=STDOUT)
    
    for line in iter(process.stdout.readline, b''):
        print(line.rstrip())

def create_argument_file():
    """
    Create an argument file to run with robot.
    """
    global path_to_argument_file
    global tests_path
    
    tests_path = pathlib.Path(__file__).parent.absolute()
    project_path = os.path.join(tests_path, '..')

    path_to_reports = os.path.join(project_path, REPORTS_DIRECTORY)
    create_reports_directory(path_to_reports)

    path_to_argument_file = os.path.join(path_to_reports, ARGUMENT_FILE_NAME)

    argurments = open(path_to_argument_file, 'w')
    argurments.write(f'--pythonpath {tests_path}\n')
    argurments.write(f'--pythonpath {project_path}\n')
    argurments.write(f'--loglevel DEBUG\n')
    argurments.write(f'--outputdir {path_to_reports}\n')

def create_reports_directory(directory):
    try:
        os.makedirs(directory)
    except OSError:
        pass

if __name__ == '__main__':
    run_tests()