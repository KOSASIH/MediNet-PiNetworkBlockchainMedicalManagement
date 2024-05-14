# medi_net/iot/medical_supply_tracking.py

import threading
import time

class MedicalSupplyTracking:
    def __init__(self):
        self.inventory = {
            'gauze': 100,
            'syringes': 500,
            'medication_a': 200,
            'medication_b': 300
        }
        self.tracking_thread = None

    def start_tracking(self):
        # Simulate real-time medical supply tracking using a thread
        self.tracking_thread = threading.Thread(target=self.track_supplies)
        self.tracking_thread.start()

    def stop_tracking(self):
        # Stop the tracking thread
        self.tracking_thread.join()

    def track_supplies(self):
        while True:
            # Simulate checking inventory levels and alerting staff when supplies are low
            for item, threshold in [('gauze', 50), ('syringes', 100), ('medication_a', 50), ('medication_b', 50)]:
                if self.inventory[item] <= threshold:
                    print(f"ALERT: {item} levels are low! Current inventory: {self.inventory[item]}")

            # Sleep for a random interval to simulate real-time tracking
            time.sleep(np.random.randint(1, 60))
