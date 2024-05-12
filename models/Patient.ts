// Improved code
class Patient {
  /**
   * @param {string} name
   * @param {number} age
   * @param {string[]} medicalHistory
   */
  constructor(name, age, medicalHistory) {
    this.name = name;
    this.age = age;
    this.medicalHistory = medicalHistory;
  }

  /**
   * Returns the patient's medical history
   * @returns {string[]}
   */
  getMedicalHistory() {
    return [...this.medicalHistory]; // Return a copy of the array
  }
}

export default Patient;
