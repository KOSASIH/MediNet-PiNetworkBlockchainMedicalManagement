from typing import List, Dict

from medinet.models import Appointment

class AppointmentService:
    """Appointment service for MediNet"""

    def __init__(self):
        self.appointments: List[Appointment] = []

    def create_appointment(self, appointment: Appointment) -> None:
        """Create a new appointment"""
        self.appointments.append(appointment)

    def get_appointments(self) -> List[Appointment]:
        """Get all appointments"""
        return self.appointments

    def update_appointment(self, appointment_id: int, updated_appointment: Appointment) -> None:
        """Update an existing appointment"""
        for index, appointment in enumerate(self.appointments):
            if appointment.id == appointment_id:
                self.appointments[index] = updated_appointment
              break

    def delete_appointment(self, appointment_id: int) -> None:
        """Delete an existing appointment"""
        for index, appointment in enumerate(self.appointments):
            if appointment.id == appointment_id:
                del self.appointments[index]
                break
