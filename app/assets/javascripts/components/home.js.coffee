@Home= React.createClass
  render: ->
    React.DOM.div
      className: 'homes'
      React.DOM.h1
        className: 'title'      
        'HelloWorld from home page'
      React.DOM.a
        className: 'linkToAnalysis'
        href: '/analyses'
        'This is a link?'
