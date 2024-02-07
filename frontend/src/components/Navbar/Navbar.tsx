import "./Navbar.css"

interface Props {
  page: number;
  changePage: (index: number) => void;
}


const Navbar = ({page, changePage}:Props) => {
  const pages: string[] = ["[ Identify ]", "[ Share ]", "[ Donate ]"]
  return (
    <div className="nav">
      <h1>Microbe Hub</h1>
      <ul className="nav-list">
      {pages.map((item: string, index: number) => (
      <li className={index===page? "nav-item active": "nav-item"} key={index} onClick={() => changePage(index)}>
         {item} 
      </li>
      ))} 
      </ul>
    </div>
  )
}

export default Navbar
