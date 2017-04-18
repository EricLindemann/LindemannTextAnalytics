class AnalysesController < ApplicationController


    def index
      $output = Array.new
      path = File.expand_path('../../../data/testWordListFile.txt', __FILE__)
      File.open(path).each do |line|
          $output.append(line)
      end
      @analyses = $output
    end

    def show
      word1 = ''
      params.each do |key, value|
        word1 = value
      end
      msg = Array.new
      indexOfWord1 = $output.index(word1 + "\n")
      path = File.expand_path('../../../data/test3LevelFile.txt', __FILE__)
      File.open(path).each do |line|
          tempArray = line.split(" ")
          if tempArray[0] == indexOfWord1.to_s
            i = 1
            while i < tempArray.length do
              if tempArray[i] == ';'
                  i += 1
                  msg << tempArray[i]
              end
              i += 1
            end        
            break
          end
      end
      i = 0
      while i < msg.length do
        msg[i] = $output[msg[i].to_i]
        i += 1
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
