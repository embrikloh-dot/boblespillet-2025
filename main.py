import tkinter as tk
import time
from random import randint
from ring import Ring
from hjelpefunksjoner import (
    handleKeyPress,
    processKeypress,
    sjekkTeleportering,
    tegnBall,
    slettBall,
    handle_avslutt,
)

# ----------------- Vindu -----------------

window = tk.Tk()
window.title("Boblespillet")
window.focus_force()

bredde = 800
hoyde = 700
canvas_height = hoyde - 150
canvas_width = bredde

window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF")
window.pack_propagate(False)

# ----------------- Topp -----------------

topp = tk.Frame(window, height=50, width=bredde * 0.75, background="#FFFFFF")
topp.pack_propagate(False)
topp.pack()

overskrift = tk.Label(
    topp,
    text="Spis mindre bobler, pass deg for de store!",
    font=("Aptos", 20),
    background="#FFFFFF",
)
overskrift.pack()

utskrift = tk.Label(
    window,
    text="Poeng: 0",
    font=("Aptos", 14),
    background="#FFFFFF",
)
utskrift.pack()

# ----------------- Canvas -----------------

canvas = tk.Canvas(
    window,
    width=bredde,
    height=canvas_height,
    background="#292b52",
)
canvas.pack(expand=True)

# ----------------- Bunn -----------------

bunn = tk.Frame(window, width=bredde, height=50, background="#3e3e3e")
bunn.pack_propagate(False)
bunn.pack()

avslutt = tk.Button(
    bunn,text="Avslutt",
    command=lambda: handle_avslutt(window, state),
)
avslutt.pack()

# ----------------- Spilltilstand -----------------

state = {
    "dx": 0,
    "dy": 0,
    "x_step": 6,
    "y_step": 6,
    "isRunning": True,
}

# Startposisjon for ball
R = 20
xpos = canvas_width // 2
ypos = canvas_height // 2

# Tastaturbinding
window.bind("<KeyPress>", lambda e: handleKeyPress(e, state))

# Hvis Ring bruker canvas
Ring.canvas = canvas

# ----------------- Spill-loop -----------------

dt = 1 / 30
last_time = time.time()

def game_loop():
    global xpos, ypos

    if not state["isRunning"]:
        return

    now = time.time()
    if now - last_time >= dt:
        slettBall(canvas)

        xpos += state["dx"]
        ypos += state["dy"]

        dx, dy, xpos, ypos = sjekkTeleportering(
            xpos,
            ypos,
            state["dx"],
            state["dy"],
            R,
            canvas_width,
            canvas_height,
        )

        state["dx"] = dx
        state["dy"] = dy

        tegnBall(canvas, xpos, ypos, R)

    window.after(int(dt * 1000), game_loop)

# ----------------- Start -----------------

game_loop()
window.mainloop()