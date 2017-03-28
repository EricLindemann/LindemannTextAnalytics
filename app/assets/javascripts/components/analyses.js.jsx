class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
  }

  render() {
    return (
      <div>
        <h1>
          {this.state.data}
        </h1>
      </div>
    );
  }
}