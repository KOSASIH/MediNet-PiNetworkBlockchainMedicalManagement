const express = require('express');
const router = express.Router();
const { DoctorContract } = require('../contracts');

// Initialize DoctorContract instance
const doctorContract = new DoctorContract(provider, process.env.DOCTOR_CONTRACT_ADDRESS);

// Get all doctors
router.get('/', async (req, res) => {
  const doctors = await doctorContract.getAllDoctors();
  res.json(doctors);
});

// Get doctor by ID
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  const doctor = await doctorContract.getDoctorById(id);
  res.json(doctor);
});

// Register doctor
router.post('/', async (req, res) => {
  const { name, specialization } = req.body;
  const tx = await doctorContract.registerDoctor(name, specialization);
  await tx.wait();
  res.status(201).send('Doctor registered successfully');
});

// Update doctor
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { name, specialization } = req.body;
  const tx = await doctorContract.updateDoctor(id, name, specialization);
  await tx.wait();
  res.send('Doctor updated successfully');
});

// Delete doctor
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  const tx = await doctorContract.deleteDoctor(id);
  await tx.wait();
  res.send('Doctor deleted successfully');
});

module.exports = router;
