import express from 'express';

const app = express();
const port = process.env.PORT || 1245;

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

export default app;
