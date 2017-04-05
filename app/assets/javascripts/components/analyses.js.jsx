class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
    this.handleClickList1 = this.handleClickList1.bind(this);
  }


  handleClickList1(word1) {
    console.log(word1);
  }


  render() {
    return (
      <div className = 'analysismain'>
        <TopBar />
        <FloatingList 
          data = {this.state.data} 
          onWordClick = {this.handleClickList1}  />
        <FloatingList data = {this.state.data} />
      </div>
    );
  }
}