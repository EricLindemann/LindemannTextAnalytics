class AnalysesController < ApplicationController


    def index
      output = Array.new
      path = File.expand_path('../../../test.txt', __FILE__)
      File.open(path).each do |line|
          output.append(line)
      end
      my_hash = {:hello => "goodbye"}
      puts output
      @analyses = output
    end

    def show
      params.each do |key, value|
        puts "#{value}"
      end
      msg = Array.new
      path = File.expand_path('../../../test.txt', __FILE__)
      File.open(path).each do |line|
          msg.append(line)
      end
      render :json => msg
    end
#    def parseText
#      output = Array.new
#      tempArray = Array.new
#      myJson = {}
#      path = File.expand_path('../../../test.txt', __FILE__)
#      File.open(path).each do |line|
#        tempArray = line.split(" ")
#        tempWord1 = tempArray[0]
###        i = 1
#        while i < tempArray.length
#          if tempArray[i] == ';'
#              i += 1
###              tempWord2 = tempArray[i]
#              myJson[tempWord1] += tempWord2
#          end
#          if tempArray[i] == ','
#              i += 1
#              myJson[tempWord1][tempWord2] += tempArray[i]
#          i++
#          end
#        end
#      return myJson    
#    
#    end

end
