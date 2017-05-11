

class FloatingList extends React.Component {  
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);   
    this.state = {active: false}    
  }

  handleChange(e) {
    this.props.onWordClick(e);
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
            {words.map((word, index) =>
              <li key={index} name ={word.toString() + this.props.listName} >
              {this.props.listName === 'List3' ? 
                <a
                  data = {this.props.documentIndex[index]}
                  className = 'default'
                  //make ref callback this is legacy
                  value={word}
                  onClick = {this.handleChange}> 
                  {word}
                
                </a>
              : 
                <a
                  className = 'default'
                  //make ref callback this is legacy
                  value={word}
                  onClick = {this.handleChange}> 
                  {word}
                
                </a>
              }
              </li>
              
            )}
          </ul>      
        </div>
      );
    }
  }
}