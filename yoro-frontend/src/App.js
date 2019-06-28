import React from "react";
import logo from "./logo.svg";
import "./App.css";
import MediaCard from "./components/media-cards/media-cards";
import ProfileDisplay from "./components/profile-display/profile-display";
import TableList from "./components/table-list/table-list";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentPerson: { first_name: "", last_name: "", profile_pic: null }
    };
  }
  myCallback = dataFromChild => {
    console.log("mycallback", dataFromChild);
    this.setState({ currentPerson: dataFromChild });
  };
  render() {
    return (
      <div className="App">
        <img src={require('./image/ciscoLogo.PNG')} className="ciscoLogo" />
        <header className="App-header" />
        <div className="Body-Border">
          <div className="Media-Card">
            <div className="Left-Card">
              <MediaCard />
            </div>
            <div className="Right-Card">
              <ProfileDisplay person={this.state.currentPerson} />
            </div>
          </div>
          <TableList callbackFromParent={this.myCallback} />
        </div>
      </div>
    );
  }
}

export default App;
