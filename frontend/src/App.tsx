import './App.css'
import Navbar from './components/Navbar/Navbar'
import { useState } from 'react';
import Model from './components/Model/Model';

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
       <Model/>
      </div>
    </>
  )
}

export default App
