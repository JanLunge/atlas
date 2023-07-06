import multiprocessing
import subprocess
import signal
import sys

processes = []

def handle_termination(signum, frame):
    # Terminate all subprocesses
    print("🛑 Terminating all modules...")
    for process in processes:
        process.terminate()
    sys.exit(0)

if __name__ == '__main__':
    import subprocess

    scripts = ['text_to_speech.py', 'ai.py', 'audio_satelite.py', 'commands.py', 'hotword_detect.py', 'speech_to_text.py']

    for script in scripts:
        process = subprocess.Popen(["python3", "src/"+script])
        print("🚀 started module", process.pid, script)
        processes.append(process)

    # Register the signal handler for termination signals
    signal.signal(signal.SIGINT, handle_termination)
    signal.signal(signal.SIGTERM, handle_termination)

    # Wait for user to exit
    input("ℹ️ Press Enter to exit...\n waiting for all 6 modules to start...\n")

    # Terminate all subprocesses
    handle_termination(None, None)
    # import audio_satelite
    # import hotword_detect
    # t = [
    #     threads.ThreadBase(audio_satelite.run),
    #     threads.ThreadBase(hotword_detect.run),
    # ]
    # for x in t:
    #     print('starting thread', x)
    #     x.start()
    # print('lol')