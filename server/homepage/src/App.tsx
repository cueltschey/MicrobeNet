import './App.css'
import Navbar from './components/Navbar/Navbar'
import { useState } from 'react'


function App() {
  const [page, setPage] = useState(0);
  const changePage = (index: number) => {
    setPage(index);
  }
  const pages = ["Classify", "Learn", "Donate", "More"]
  document.title = "testing"
  return (
    <>
      <Navbar page={page} changePage={changePage} pages={pages} />
    </>
  )
}

export default App
