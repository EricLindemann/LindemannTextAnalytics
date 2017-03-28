@Home= React.createClass

  closeNav: ->
    console.log(document.getElementById("mySideNav").style.width)
    this.refs.mySideNav.style.width = 0
    console.log(document.getElementById("mySideNav").style.width)
    
  openNav: ->
    this.refs.mySideNav.style.width = 250
    console.log(this.refs.mySideNav.style.width)



  render: ->
    React.DOM.div
      id:'main'

      React.DOM.div
        id: 'mySideNav'
        className: 'sidenav'
        React.DOM.button
          className: 'closebtn'
          onClick: @closeNav
          'click'
        React.DOM.a
          className: 'Analyses'
          href: '#'
          'Analysis'
    
      React.DOM.h1
        className: 'title'      
        'HelloWorld from home page'
      React.DOM.button
        className: 'openNavButton'
        onClick: @openNav
        'Open Nav'



