const express = require('express');
const bodyParser = require('body-parser');
const tf = require('@tensorflow/tfjs-node');
const { createCanvas, loadImage } = require('canvas');

const app = express();
const PORT = 3000;

// Middleware to parse JSON and URL-encoded bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('../dist/'));

// Load your pre-trained TensorFlow model
const modelPath = '../../model/Model-v1/trained_model.h5';

const getModel = async () => {
  const model = await tf.loadLayersModel(`file://${modelPath}`);
  return model
}


// Define a route for image evaluation
app.post('/evaluate-image', async (req, res) => {
  try {
    const model = getModel();
    // Get the image data from the request body
    const imageData = req.body.imageData; // Assuming imageData is a base64 encoded image

    // Load image using canvas
    const canvas = createCanvas();
    const ctx = canvas.getContext('2d');
    const img = new Image();
    img.src = imageData;
    ctx.drawImage(img, 0, 0);

    // Convert canvas image to tensor
    const imageTensor = tf.browser.fromPixels(canvas);

    // Resize and preprocess the image data
    const resizedImageTensor = tf.image.resizeBilinear(imageTensor, [targetHeight, targetWidth]);
    const preprocessedImageTensor = resizedImageTensor.div(255.0); // Normalize pixel values

    // Make prediction using the model
    const prediction = model.predict(preprocessedImageTensor);

    // Convert prediction to JSON and send as response
    res.json({ prediction: prediction.dataSync() });
  } catch (error) {
    console.error('Error evaluating image:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
