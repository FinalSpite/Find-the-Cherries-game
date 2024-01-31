import subprocess
import tempfile
import os
def quit():
    try:
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(['ps','A'], stdout=tempf)
            proc.wait()
            tempf.seek(0)
            output = tempf.read()

        output = str(output)

        output = output.split()

        for i in range(3):
            print("\n")
            
        print(output.index("Launcher.app/Contents/MacOS/Python"))

        index = (output.index("Launcher.app/Contents/MacOS/Python")-6)

        PID = output[index]

        print(PID)

        bruh = PID.split('\\n')

        print(bruh[1])

        os.system(f"kill {bruh[1]}")
    except: #noqa
        pass
if __name__ == "__main__":
    quit()