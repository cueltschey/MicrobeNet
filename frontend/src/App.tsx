import './App.css'
import Navbar from './components/Navbar/Navbar'
import React, { useState } from 'react';
import ImageUploader from './components/Model/ImageProcess';

function App() {
  const [page, setPage] = useState(0);
  const changePage = (index: number) => {
    setPage(index);
    window.scroll(0,0)
  }

  return (
    <>
       <Navbar page={page} changePage={changePage}/> 
      <div className='main'>
       <ImageUploader/>
      </div>
    </>
  )
}

export default App
