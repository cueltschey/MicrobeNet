import { useState, ChangeEvent } from 'react';
import "./Model.css"


const Model = () => {
  const [selectedImage, setSelectedImage] = useState<File | null>(null);

  const handleImageChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];

    if (file) {
      setSelectedImage(file);
      console.log(file.name)
    }
  };

  const handleSubmit = async () => {
    if (selectedImage) {
      const form = new FormData()
      form.append('file', selectedImage)

      fetch('http://localhost:3001/upload', {
        method: 'POST',
        body: form,
      })
        .then(response => response.json())
        .then(data => {
          // Handle the response data as needed
          console.log('Response:', data);
        })
        .catch(error => {
          console.error('Error:', error);
        });    }
  };

  return (
    <>
    <div className='img-upload'>
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
      />
      {selectedImage && (
        <div>
          <img src={URL.createObjectURL(selectedImage)} alt={selectedImage.name} style={{ maxWidth: '100%', maxHeight: '100%' }} />
        </div>
      )}
      <button onClick={handleSubmit}>Submit</button>
    </div>
    <div className='results'>

    </div>
    </>
  );
};

export default Model;
