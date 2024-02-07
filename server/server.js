const express = require('express');
const path = require('path');
const multer = require('multer')
const os = require('os')

const app = express();
const port = 3001;

const upload = multer({dest:os.tmpdir()})

app.use(express.static(path.join(__dirname, '../frontend/dist/')));

app.post('/upload', upload.single('image'), (req, res) => {
  const file = req.file;

  console.log(file)

  res.sendStatus(200)
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/dist/', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server is running on  http://localhost:${port}`);
});

