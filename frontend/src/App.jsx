import { useState, useEffect } from 'react'
import './App.css'
import About from './components/About'
import Nav from './components/Navbar'
import Signup from './components/Signup'

function App() {
  const [page, changePage] = useState();

  const renderPage = () => {
    switch (page) {
      case "a" : return "a"; 
      case "signup" : return <Signup />;
      default : return <About />;
    }
  }
  const [pagedata, changePagedata] = useState(renderPage());

  useEffect(() => {
    changePagedata(renderPage());
  }, [page]);

  return (
    <>
      <Nav changePage = { changePage }/>
      { pagedata }
    </>
  );

};

export default App;
