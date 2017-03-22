@Analysis = React.createClass
  getInitialState: ->
    analyses: @props.data
  getDefaultProps: ->
    records: []

  render: ->
    test = @state.analyses
    console.log(test)
    React.DOM.div
      className: 'analyses'
      React.DOM.h1
        className: 'title'      
        'Hello from React'

      React.DOM.h1
        className: 'title'
        @state.analyses
