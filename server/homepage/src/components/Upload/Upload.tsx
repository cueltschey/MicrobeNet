// Upload.js

import { useState } from 'react';

const Upload = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e: any) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
  };

  const handleSubmit = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await fetch('/classify', {
        method: 'POST',
        body: formData,
      });
      // Handle response as needed
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload</button>
    </div>
  );
};

export default Upload;

