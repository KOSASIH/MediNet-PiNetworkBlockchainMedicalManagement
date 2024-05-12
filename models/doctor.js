// Improved code
class Doctor {
  /**
   * @param {string} name
   * @param {string} specialty
   */
  constructor(name, specialty) {
    this.name = name;
    this.specialty = specialty;
  }

  /**
   * Returns the doctor's specialty
   * @returns {string}
   */
  getSpecialty() {
    return this.specialty;
  }
}

export default Doctor;
