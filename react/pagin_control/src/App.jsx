import React from 'react'
import './App.css'

function Mybutton(){
  return (
    <button>
      Botão de teste
    </button>
  );
}

function App() {

  return (
    <>
      <div>
        <h1>Olá mundo react</h1>
        <Mybutton />
      </div>
    </>
  );
}

export default App
