class FloatingList extends React.Component {  
  constructor(props) {
    super(props);
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

          </ul>      
        </div>
      );
    }
    else {
      return (
        <div name = {this.props.listName} className = 'floatinglist'>
          <ul>
            {words.map((word) =>
              <li key={word.toString() + this.props.listName} name ={word.toString() + this.props.listName} >
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