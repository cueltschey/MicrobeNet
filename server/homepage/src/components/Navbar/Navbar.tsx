import "./Navbar.css"


interface input {
  page: number;
  changePage: (index: number) => void;
  pages: string[];
}

const Navbar = ({ page, changePage, pages }: input) => {
  return (
    <div className="navbar">
      <ul className="navlist">
        {pages.map((text: string, index: number) => (
          <li key={index} onClick={() => changePage(index)} className={page === index ? "navitem active" : "navitem"}>{text}</li>
        ))}
      </ul>
    </div>
  )
}

export default Navbar
