// server.js

const express = require('express');
const multer = require('multer');
const tf = require('@tensorflow/tfjs-node');
const path = require('path')
const fs = require('fs')

const app = express();
const port = 3000;

app.use(express.static(path.join("/home/chasuelt/Desktop/MicrobeNet/server/", "homepage/dist")))
app.use(express.json())

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'images/')
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname)
  },
})
const upload = multer({ storage: storage })



// Load your model here
const get_model = async () => {
  const model = tf.loadLayersModel('file:///home/chasuelt/Desktop/Trained_Models/MicrobeNetV3/MicrobeNetV3_unclassified.h5'); 
  console.log(model.summary())
  return model
}

const read_image = (image_path) => {
  const buffer = fs.readFileSync(image_path);
  return tf.node.decodeJpeg(buffer);
}

app.get("/", (req, res) => {
  res.sendFile(path.join("/home/chasuelt/Desktop/MicrobeNet/server/", "hompage/dist"))
})


// POST endpoint for image classification
app.post('/classify', upload.single('image'), async (req, res, cb) => {
  try {
    const image = req.file;
    console.log(image)
    // load the model
    const model = get_model()
    // Load the image from the request
    const tensor = read_image(image.path)

    // Preprocess the image as needed (resize, normalize, etc.)
    // For example:
    const processedImage = tensor.resizeBilinear([224, 224]).toFloat().div(tf.scalar(255));

    // Perform classification using your model
    const prediction = model.predict(processedImage);

    // Send back the prediction result
    res.json(prediction);
    res.sendStatus(200);
  } catch (error) {
    console.error('Error classifying image:', error);
    res.status(500).json({ error: 'An error occurred while processing the image.' });
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

