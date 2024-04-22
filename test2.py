import tkinter as tk

class VAGui:
    @staticmethod
    def get_rgb_values(color):
        # Function to retrieve RGB values from a color string (e.g., "#RRGGBB")
        if color.startswith("#") and len(color) == 7:
            return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        else:
            # Invalid color format, return default black
            return (0, 0, 0)
        
    @staticmethod
    def changeBGcolor(canvas, current_color, target_color, delay, steps):
        # Function to fade the background color of a canvas from current_color to target_color
        r_step = (target_color[0] - current_color[0]) / steps
        g_step = (target_color[1] - current_color[1]) / steps
        b_step = (target_color[2] - current_color[2]) / steps
        
        def fade_color(step):
            if step <= steps:
                print("Changing")
                new_color = (
                    int(current_color[0] + r_step * step),
                    int(current_color[1] + g_step * step),
                    int(current_color[2] + b_step * step)
                )
                canvas.config(bg='#{:02x}{:02x}{:02x}'.format(*new_color))
                canvas.after(delay, fade_color, step + 1)
        
        fade_color(1)

# Example usage:
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, bg="black")
canvas.pack()

VAGui.changeBGcolor(canvas=canvas,
                    current_color=VAGui.get_rgb_values(canvas.cget("background")),
                    target_color=(255, 255, 255),
                    delay=50,
                    steps=10)

root.mainloop()
