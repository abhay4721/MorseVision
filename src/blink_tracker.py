# src/blink_tracker.py
import time

class BlinkTracker:
    def __init__(self):
        self.eye_closed_time = None
        self.last_symbol = ""

    def update(self, eye_closed: bool):
        """
        eye_closed = True if eyes are closed
        eye_closed = False if eyes are open
        """
        current_time = time.time()

        
        if eye_closed and self.eye_closed_time is None:
            self.eye_closed_time = current_time

        
        elif not eye_closed and self.eye_closed_time is not None:
            duration = current_time - self.eye_closed_time
            self.eye_closed_time = None

            if duration < 0.4:
                self.last_symbol = "."
            else:
                self.last_symbol = "-"

            return self.last_symbol

        return None
