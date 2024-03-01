import "./Upload.css"
import axios from "axios";

const Upload = () => {
  const handleFileUpload = (event: any) => {
    // get the selected file from the input
    const file = event.target.files[0];
    // create a new FormData object and append the file to it
    const formData = new FormData();
    formData.append("image", file, file.name);
    // make a POST request to the File Upload API with the FormData object and Rapid API headers
    axios
      .post("/classify", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          'Accept-Language': 'en-US,en;q=0.8',
        },
      })
      .then((response) => {
		// handle the response
        console.log(response);
      })
      .catch((error) => {
        // handle errors
        console.log(error);
      });
  };
  // render a simple input element with an onChange event listener that calls the handleFileUpload function
  return (
    <div>
      <input type="file" onChange={handleFileUpload} />
    </div>
  );
};
export default Upload;
