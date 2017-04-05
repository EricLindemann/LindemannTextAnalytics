class FloatingList extends React.Component {  
  constructor(props) {
    super(props);
    this.state = {data: this.props.data};
    
  }

    render() {
    const words = this.state.data;
    const listItems = words.map((words) =>
      <ul key={words.toString()} >
        <a className = 'floatingList' href = '/'>
          {words}
        </a>
      </ul>
    );
    return (
      <div className = 'floatinglist' id= 'firstWords'>
          {listItems}
      </div>
    );
  }
}