import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import { subscribeToTimer } from "../../sockets/table-socket/table-socket";

const styles = {
  tableRow: {
    "&$hover:hover": {
      backgroundColor: "blue"
    }
  },
  root: {
    width: "100%",
    marginTop: "30px",
    overflowX: "auto"
  },
  table: {
    minWidth: 650
  }
};
// http://4fd2bcd1.ngrok.io/yoro/getListOfCheckedIn
class TableList extends React.Component {
  componentDidMount() {
    fetch("http://4fd2bcd1.ngrok.io/yoro/getListOfCheckedIn", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ id: "5d1387b338fd21e" })
    })
      .then(res => res.json())
      .then(data => {
        this.setState({ rows: data.result });
      })
      .catch(console.log);
  }
  constructor(props) {
    super(props);
    this.state = { rows: [] };

    subscribeToTimer((err, res) => {
      let newRow = this.state.rows;
      newRow.unshift(
        this.createData(
          res.cec_id,
          res.checked_in,
          res.first_name,
          res.last_name,
          res.registered
        )
      );
      this.setState({
        rows: newRow
      });
    });
  }

  createData(cec_id, checked_in, first_name, last_name, registered) {
    return { cec_id, checked_in, first_name, last_name, registered };
  }

  //   rows = [];
  render() {
    return (
      <Paper className={this.props.classes.root}>
        <Table className={this.props.classes.table}>
          <TableHead>
            <TableRow>
              <TableCell>Cec</TableCell>
              <TableCell align="right">Checked In</TableCell>
              <TableCell align="right">First Name</TableCell>
              <TableCell align="right">Last Name</TableCell>
              <TableCell align="right">Registered</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.rows.map(row => (
              <TableRow
                key={row.cec_id}
                className={this.props.classes.tableRow}
              >
                <TableCell component="th" scope="row">
                  {row.cec_id}
                </TableCell>
                <TableCell align="right">{row.checked_in}</TableCell>
                <TableCell align="right">{row.first_name}</TableCell>
                <TableCell align="right">{row.last_name}</TableCell>
                <TableCell align="right">{row.registered}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    );
  }
}
export default withStyles(styles)(TableList);
