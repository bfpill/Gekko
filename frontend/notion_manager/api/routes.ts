import express from 'express';

import notionServices from './notionServices';

const router = express.Router();

router.post("/", notionServices.addItem("I LOVE GEKKO"));

// Export router
export default router;