class FloatingList extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
    this.handleChange = this.handleChange.bind(this);   
    
  }


  handleChange(e) {
    this.props.onWordClick(e.target.getAttribute('value'));
  }

  render() {
    words = this.props.data
    if (words == '') {
      return (
        <div className = 'floatinglist'>
          <ul>
            <li key={words.toString()}>

            </li>
          
          </ul>      
        </div>
      );
    }
    else {
      console.log(words)
      return (
        <div className = 'floatinglist'>
          <ul>
            {words.map((word) =>
              <li key={word.toString()}>
                <a 
                  value={word}
                  onClick = {this.handleChange}> 
                  {word}
                
                </a>
              </li>
              
            )}
          </ul>      
        </div>
      );
    }
  }
}