class AnalysesController < ApplicationController
    def index
      #@analyses = Analysis.all
      #path = File.expand_path('../../../', __FILE__)
      #output = `python #{path}/hello_world.py`
      output = Array.new
      path = File.expand_path('../../../test.txt', __FILE__)
      File.open(path).each do |line|
          output.append(line)
      end
      @analyses = output
    end
end
