import {StrictMode, useEffect} from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";


import App from './App.jsx'
import ChatInterface from "./chat-component.jsx";

const AudioPlayer = () => {
  useEffect(() => {
    let audio = null;

    // Create the audio element but don't play it yet
    audio = new Audio();
    audio.src = 'assets/Lofi_Hip_Hop__BPM90.mp3';
    audio.loop = true;

    // This function will only be called after user interaction
    const handleUserInteraction = () => {
      console.log('User interaction detected, attempting to play audio');

      audio.play()
        .then(() => {
          console.log('Audio playing successfully');
          // Remove event listeners once audio is playing
          window.removeEventListener('click', handleUserInteraction);
          window.removeEventListener('keydown', handleUserInteraction);
        })
        .catch(error => {
          console.error('Audio playback failed:', error);
        });
    };

    // Add event listeners for common user interactions
    window.addEventListener('click', handleUserInteraction);
    window.addEventListener('keydown', handleUserInteraction);

    // Cleanup function
    return () => {
      if (audio) {
        audio.pause();
        audio.src = '';
      }

      window.removeEventListener('click', handleUserInteraction);
      window.removeEventListener('keydown', handleUserInteraction);
    };
  }, []); // Empty dependency array means this effect runs once on mount

  return null; // This component doesn't render anything
};

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <AudioPlayer />
        <App/>
        {/*<ChatInterface/>*/}
    </StrictMode>,
)