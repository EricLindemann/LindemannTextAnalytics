

class FloatingList extends React.Component {  
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);   
    this.state = {active: false}    
  }

  handleChange(e) {
    //console.log(this)
    //e.preventDefault();
    //if (this.state.active != 'a'){
      //this.state.active.target.className = ''
    //}
    for (var ref in this.refs) {
        this.refs[ref].className = 'default';
    }
    e.target.className = 'highlight';
    this.setState({active: true})
    //console.log(e.target.getAttribute('class'));
    //this.setState({active: e});
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
            {words.map((word, index) =>
              <li key={index} name ={word.toString() + this.props.listName} >
                <a
                  className = 'default'
                  //make ref callback this is legacy
                  ref = {word}
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