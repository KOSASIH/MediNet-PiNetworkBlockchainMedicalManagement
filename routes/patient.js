const express = require('express');
const router = express.Router();
const { PatientContract } = require('../contracts');

// Initialize PatientContract instance
const patientContract = new PatientContract(provider, process.env.PATIENT_CONTRACT_ADDRESS);

// Get all patients
router.get('/', async (req, res) => {
  const patients = await patientContract.getAllPatients();
  res.json(patients);
});

// Get patient by ID
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  const patient = await patientContract.getPatientById(id);
  res.json(patient);
});

// Register patient
router.post('/', async (req, res) => {
  const { name, dateOfBirth } = req.body;
  const tx = await patientContract.registerPatient(name, dateOfBirth);
  await tx.wait();
  res.status(201).send('Patient registered successfully');
});

// Update patient
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { name, dateOfBirth } = req.body;
  const tx = await patientContract.updatePatient(id, name, dateOfBirth);
  await tx.wait();
  res.send('Patient updated successfully');
});

// Delete patient
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  const tx = await patientContract.deletePatient(id);
  await tx.wait();
  res.send('Patient deleted successfully');
});

module.exports = router;
