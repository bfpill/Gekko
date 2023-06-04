import express from 'express';

import notionController from "./notionController"

const router = express.Router();

router.post("/", notionController.addItem);

// Export router
export default router;