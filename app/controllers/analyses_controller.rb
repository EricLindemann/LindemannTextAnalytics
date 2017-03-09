class AnalysesController < ApplicationController
    def index
      #@analyses = Analysis.all
      path = File.expand_path('../../../', __FILE__)
      output = `python #{path}/hello_world.py`
      @analyses = output
    end
end
