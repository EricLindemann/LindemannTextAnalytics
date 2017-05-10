class Analysis extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {word1List: this.props.data,
                  word1: '',
                  word2List: '',
                  word2: '',
                  documentList: '',
                  documentIndexes: '',
                  document: ''};
    this.handleClickList1 = this.handleClickList1.bind(this);
    this.handleClickList2 = this.handleClickList2.bind(this);    
    this.handleDocumentClick = this.handleDocumentClick.bind(this);
  }

  componentDidMount()
  {
    document.title = "Analysis"
  }


  handleClickList1(word) {
    this.setState({word1: word})
    this.setState({documentList: ''})
    urlWord1 = 'analyses/' + word
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


  handleClickList2(word) {
    this.setState({word2: word})

    urlWord1 = 'analyses/' + this.state.word1 + '+' + word
    $.ajax({
      url: urlWord1,
      dataType: 'json',
      type: 'GET',
      success: function(result){
        this.setState({documentList: result.names,
                      documentIndexes: result.indexes
                      });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  }


  handleDocumentClick(documentIndex) {
    urlWord1 = 'analyses/' + this.state.word1 + '+' + this.state.word2 + '+' + documentIndex
    $.ajax({
      url: urlWord1,
      dataType: 'json',
      type: 'GET',
      success: function(result){
        this.setState({document: result});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)

    });
  }


  render() {
    return (
      <div className = 'analysismain'>
        <TopBar />
        <FloatingList 
          data = {this.state.word1List} 
          onWordClick = {this.handleClickList1}
          listName = "List1"  />
        <FloatingList 
          data = {this.state.word2List} 
          onWordClick = {this.handleClickList2}
          listName = "List2"  />
        <FloatingList 
          data = {this.state.documentList} 
          onWordClick = {this.handleDocumentClick}
          documentIndex = {this.state.documentIndexes}
          listName = "List3"  />
        <br />          

        {this.state.document}

      </div>
    );
  }
}