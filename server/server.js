// server.js

const express = require('express');
const multer = require('multer');
const tf = require('@tensorflow/tfjs-node');
const path = require('path')

const app = express();
const port = 3000;

app.use(express.static(path.join(".", "homepage/dist")))

// Multer middleware for handling multipart/form-data (file uploads)
const upload = multer({ dest: 'uploads/' });

// Load your model here
const get_model = async () => {
  return await tf.loadLayersModel('path/to/your/model.h5'); // change this .h5 path
}

const read_image = (buffer) => {
  return tf.node.decodeImage(buffer);
}

app.get("/", (req, res) => {
  res.sendFile(path.join(".", "hompage/dist"))
})


// POST endpoint for image classification
app.post('/classify', upload.single('image'), async (req, res) => {
  try {
    // load the model
    const model = get_model()
    // Load the image from the request
    const image = read_image(req.file.buffer)

    // Preprocess the image as needed (resize, normalize, etc.)
    // For example:
    const processedImage = image.resizeBilinear([224, 224]).toFloat().div(tf.scalar(255));

    // Perform classification using your model
    const prediction = model.predict(processedImage);

    // Send back the prediction result
    res.json(prediction);
  } catch (error) {
    console.error('Error classifying image:', error);
    res.status(500).json({ error: 'An error occurred while processing the image.' });
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

