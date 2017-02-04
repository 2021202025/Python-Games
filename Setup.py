import cx_Freeze

executables = [cx_Freeze.Executable("Snakiee.py")]

cx_Freeze.setup(
    name = "Snakie",
    options={"build_exe":{"packages":["pygame"], "include_files":["Apple.png","Snakiee3.png"]}},

    description = "Snake Game",
    executables = executables
    )
