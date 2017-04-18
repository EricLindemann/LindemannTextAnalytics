class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {word1List: this.props.data,
                  word1: '',
                  word2List: '',
                  word2: '',
                  documentList: '',
                  document: ''};
    this.handleClickList1 = this.handleClickList1.bind(this);
    this.handleDocumentClick = this.handleDocumentClick.bind(this);
    this.getWord2 = this.getWord2.bind(this);
  }


  handleClickList1(word1) {
    this.getWord2(word1)
  }

  handleDocumentClick(documentName) {
    this.setState({document: documentName});
  }

  getWord2(word1) {
    urlWord1 = 'analyses/' + word1
    $.ajax({
      url: urlWord1,
      dataType: 'json',
      type: 'GET',
      success: function(result){
        this.setState({word2List: result});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)

    });
  }


  render() {

    console.log(this.state.word2List)
    return (
      <div className = 'analysismain'>
        <TopBar />
        <FloatingList 
          data = {this.state.word1List} 
          onWordClick = {this.handleClickList1}  />
        <FloatingList 
          data = {this.state.word2List} 
          onWordClick = {this.handleClickList1}  />
        <FloatingList 
          data = {this.state.documentList} 
          onWordClick = {this.handleDocumentClick}  />
        <br />          
        {this.state.document}
      </div>
    );
  }
}