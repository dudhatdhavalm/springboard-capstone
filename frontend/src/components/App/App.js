import { Component } from "react";
import axios from "axios";
import { URL } from "../../static/urls";
import "./App.css";

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
      <div className="app">
        <h1>Loan Prediction</h1>
        <form onSubmit={this.onSubmit}>
          <select
            id="ids"
            value={this.state.selectedId}
            onChange={this.onChange}
            className="form-control"
          >
            <option value="">Please select ID</option>
            {options}
          </select>
          <input type="submit" value="Predict" className="btn btn-success" />
        </form>
        {loan && (
          <div className="predict-info">
            <table className="table">
              <tr>
                <td>Id</td>
                <td>{loan.id}</td>
              </tr>
              <tr>
                <td>Actual</td>
                <td>{loan.actual ? "Approve" : "Reject"}</td>
              </tr>
              <tr>
                <td>Predict</td>
                <td>{loan.predict ? "Approve" : "Reject"}</td>
              </tr>
              <tr>
                <td>Default Probability</td>
                <td>{loan.default}</td>
              </tr>
              <tr>
                <td>None Default Probability</td>
                <td>{loan.none_default}</td>
              </tr>
            </table>
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
    if (this.state.selectedId == "") {
      alert("Please select ID");
      return;
    }
    axios.post(URL + "loan/" + this.state.selectedId).then((response) => {
      console.log(response.data);
      this.setState({ loan: response.data });
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
