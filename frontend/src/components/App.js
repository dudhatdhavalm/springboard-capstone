import { Component } from "react";
import axios from "axios";
import { URL } from "../static/urls";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ids: [],
      selectedId: "",
      loan: null,
    };
  }

  render() {
    const options = this.state.ids.map((id) => {
      return <option value={id}>{id}</option>;
    });
    const loan = this.state.loan;
    
    return (      
      <div className="App">
        <form onSubmit={this.onSubmit}>
          <select
            id="ids"
            value={this.state.selectedId}
            onChange={this.onChange}
          >
            {options}
          </select>
          <input type="submit" value="Predict" />
        </form>
        {loan && (
          <div>
            <div>id: {loan.id}</div>
            <div>Actual: {loan.actual ? "Approve": "Reject"}</div>
            <div>Predict: {loan.predict ? "Approve": "Reject"}</div>
            <div>Default Probability: {loan.default}</div>
            <div>None Default Probability: {loan.none_default}</div>
          </div>
        )}
      </div>
    );
  }

  onChange = (e) => {
    const id = e.target.value;
    this.setState({
      selectedId: id,
    });
  };

  onSubmit = (e) => {
    e.preventDefault();
    axios.post(URL + "loan/" + this.state.selectedId).then((response) => {
      console.log(response.data)
      this.setState({ loan: response.data})
    });
  };

  fetchLoanId = () => {
    axios.get(URL + "loan/id").then((response) => {
      this.setState({
        ids: response.data,
      });
    });
  };

  componentDidMount() {
    this.fetchLoanId();
  }
}

export default App;
