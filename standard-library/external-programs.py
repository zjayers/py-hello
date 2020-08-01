import subprocess

#  Legacy Methods
# subprocess.call()
# subprocess.check_call()
# subprocess.check_output()
try:
    completedProcess = subprocess.run(['ls', '-l'],
                                      capture_output=True,
                                      text=True,
                                      check=True)
    print('args', completedProcess.args)
    print('returncode', completedProcess.returncode)
    print('stderr', completedProcess.stderr)
    print('stdout', completedProcess.stdout)
except subprocess.CalledProcessError as error:
    print(error)
