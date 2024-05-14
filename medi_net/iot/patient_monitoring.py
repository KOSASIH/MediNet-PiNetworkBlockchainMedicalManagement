# medi_net/iot/patient_monitoring.py

import threading
import time

class PatientMonitoring:
    def __init__(self):
        self.vital_signs = {
            'heart_rate': 0,
            'blood_pressure': (0, 0),
            'oxygen_saturation': 0,
            'temperature': 0
        }
        self.activity_level = 0
        self.monitoring_thread = None

    def start_monitoring(self):
        # Simulate real-time patient monitoring using a thread
        self.monitoring_thread = threading.Thread(target=self.monitor_patient)
        self.monitoring_thread.start()

    def stop_monitoring(self):
        # Stop the monitoring thread
        self.monitoring_thread.join()

    def monitor_patient(self):
        while True:
            # Simulate collecting vital signs and activity level data
            self.vital_signs['heart_rate'] = self.collect_heart_rate()
            self.vital_signs['blood_pressure'] = self.collect_blood_pressure()
            self.vital_signs['oxygen_saturation'] = self.collect_oxygen_saturation()
            self.vital_signs['temperature'] = self.collect_temperature()
            self.activity_level = self.collect_activity_level()

            # Print the collected data
            print(f"Vital Signs: {self.vital_signs}")
            print(f"Activity Level: {self.activity_level}\n")

            # Sleep for a random interval to simulate real-time monitoring
            time.sleep(np.random.randint(1, 5))

    @staticmethod
    def collect_heart_rate():
        # Simulate collecting heart rate data
        return np.random.randint(60, 101)

    @staticmethod
    def collect_blood_pressure():
        # Simulate collecting blood pressure data
        return (np.random.randint(80, 121), np.random.randint(40, 91))

    @staticmethod
    def collect_oxygen_saturation():
        # Simulate collecting oxygen saturation data
        return np.random.randint(90, 101)

    @staticmethod
    def collect_temperature():
        # Simulate collecting temperature data
        return np.random.uniform(96.8, 100.4)

    @staticmethod
    def collect_activity_level():
        # Simulate collecting activity level data
        return np.random.randint(0, 6)
