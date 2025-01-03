const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, World! This is running on Google Cloud Run!');
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
