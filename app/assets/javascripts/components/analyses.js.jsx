class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
  }

  render() {
    return (
      <div id='analyses'>
        <TopBar />
        <h1>
          {this.state.data}
        </h1>
      </div>
    );
  }
}