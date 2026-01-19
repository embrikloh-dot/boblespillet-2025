"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""
"""
Ulike funksjoner som er til bruk i animasjonslogikk etc.
main.py skal helst ikke bli noe lengre.
"""

def handleKeyPress(evt, state):
    """
    Oppdaterer retning basert på tastetrykk.
    state er en dict som inneholder dx, dy, x_step, y_step og isRunning.
    """
    key = evt.keysym

    if key in ("q", "Q"):
        state["isRunning"] = False

    elif key in ("Up", "w"):
        state["dx"] = 0
        state["dy"] = -state["y_step"]

    elif key in ("Down", "s"):
        state["dx"] = 0
        state["dy"] = state["y_step"]

    elif key in ("Left", "a"):
        state["dx"] = -state["x_step"]
        state["dy"] = 0

    elif key in ("Right", "d"):
        state["dx"] = state["x_step"]
        state["dy"] = 0

    elif key == "f":
        state["dx"] = 0
        state["dy"] = 0


def processKeypress(evt):
    """Enkel debug-funksjon."""
    print(f"key: {evt.keysym}")


def sjekkTeleportering(xpos, ypos, dx, dy, R, canvas_width, canvas_height):
    """
    Teleporterer ballen når den går utenfor kanten.
    """
    if xpos - R >= canvas_width and dx > 0:
        xpos = -R
    elif xpos + R <= 0 and dx < 0:
        xpos = canvas_width + R

    if ypos - R >= canvas_height and dy > 0:
        ypos = -R
    elif ypos + R <= 0 and dy < 0:
        ypos = canvas_height + R

    return dx, dy, xpos, ypos


def tegnBall(canvas, xpos, ypos, R=50, farge="#ff9944"):
    """Tegner ballen på canvas."""
    canvas.create_oval(
        xpos - R,
        ypos - R,
        xpos + R,
        ypos + R,
        fill=farge,
        outline="",
        tags="ball"
    )


def slettBall(canvas):
    """Sletter ballen fra canvas."""
    canvas.delete("ball")


def handle_avslutt(window, state=None):
    """
    Avslutter programmet trygt.
    """
    if state is not None:
        state["isRunning"] = False
    window.destroy()
