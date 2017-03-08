class AnalysesController < ApplicationController
    def index
      @analyses = Analysis.all
    end
end
