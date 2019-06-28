import React from "react";
import logo from "./logo.svg";
import "./App.css";
import MediaCard from "./components/media-cards/media-cards";
import ProfileDisplay from "./components/profile-display/profile-display";
import TableList from "./components/table-list/table-list";

function App() {
  return (
    <div className="App">
      <header className="App-header" />
      <div className="Body-Border">
        <div className="Media-Card">
          <div className="Left-Card">
            <MediaCard />
          </div>
          <div className="Right-Card">
            <ProfileDisplay />
          </div>
        </div>
        <TableList />
      </div>
    </div>
  );
}

export default App;
