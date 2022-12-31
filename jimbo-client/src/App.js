import React, { useEffect, useState } from 'react';
import './App.css';
import logo from './logo.svg';
import Workouts from './components/Workouts';
import WorkoutsLoading from './components/WorkoutsLoading'


function App() {
  const WorkoutsComponent = WorkoutsLoading(Workouts);
  const [appState, setAppState] = useState({
    loading: false,
    workouts: null,
  });
  useEffect(() => {
    setAppState({ loading: true});
    const apiUrl = 'http://127.0.0.1:8000/api/';
    fetch(apiUrl)
      .then((response) => response.json())
      .then((workouts) => {
        setAppState({ loading: false, workouts: workouts })
      });
  }, [setAppState]);
  return (
    <div className="App">
      <h1>Your Workouts</h1>
      <WorkoutsComponent isLoading={appState.loading} workouts={appState.workouts}/>
    </div>
  )
}

export default App;