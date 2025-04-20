import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";


import App from './App.jsx'
import ChatInterface from "./chat-component.jsx";

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
      {/*<ChatInterface/>*/}
  </StrictMode>,
)
