class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
    
  }



  render() {
    return (
      <div className = 'analysismain'>
        <TopBar />
        <FloatingList data = {this.state.data} />
        <FloatingList data = {this.state.data} />
      </div>
    );
  }
}