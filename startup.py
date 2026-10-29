import subprocess
def startup_programs():
    startup_programs = [
        "fastfetch","--logo-type", "kitty"
    ]
    subprocess.run(startup_programs)
    return
    