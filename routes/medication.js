const express = require('express');
const router = express.Router();
const { MedicationContract } = require('../contracts');

// Initialize MedicationContract instance
const medicationContract = new MedicationContract(provider, process.env.MEDICATION_CONTRACT_ADDRESS);

// Get all medications
router.get('/', async (req, res) => {
  const medications = await medicationContract.getAllMedications();
  res.json(medications);
});

// Get medication by IDrouter.get('/:id', async (req, res) => {
  const { id } = req.params;
  const medication = await medicationContract.getMedicationById(id);
  res.json(medication);
});

// Register medication
router.post('/', async (req, res) => {
  const { name, manufacturer, dosage, instructions } = req.body;
  const tx = await medicationContract.registerMedication(name, manufacturer, dosage, instructions);
  await tx.wait();
  res.status(201).send('Medication registered successfully');
});

// Update medication
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { name, manufacturer, dosage, instructions } = req.body;
  const tx = await medicationContract.updateMedication(id, name, manufacturer, dosage, instructions);
  await tx.wait();
  res.send('Medication updated successfully');
});

// Delete medication
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  const tx = await medicationContract.deleteMedication(id);
  await tx.wait();
  res.send('Medication deleted successfully');
});

module.exports = router;
