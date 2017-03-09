@Analysis = React.createClass
  getInitialState: ->
    analyses: @props.data
  getDefaultProps: ->
    records: []

  render: ->
    console.log @state.analyses
    React.DOM.div
      className: 'analyses'
      React.DOM.h1
        className: 'title'      
        'Hello from React'

      React.DOM.h1
        className: 'title'
        @state.analyses
