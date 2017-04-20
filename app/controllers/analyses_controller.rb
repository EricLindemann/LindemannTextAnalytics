class AnalysesController < ApplicationController


    def index
      $wordList = Array.new
      $documentList = Array.new
      path = File.expand_path('../../../data/WordListFile.txt', __FILE__)
      File.open(path).each do |line|
          $wordList.append(line)
      end
      path = File.expand_path('../../../data/textDocuments.txt', __FILE__)
      file = File.open(path, "rb")
      
      $documentList = file.read
      $documentList = $documentList.split("ZZZ")
      $wordList = $wordList.map {|x| x.chomp}
      @analyses = $wordList
    end

    def show
      msg = Array.new      
      word = ''
      params.each do |key, value|
        word = value
      end
      words = word.split("+")
      if words.length == 1
        indexOfWord1 = $wordList.index(word)
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
          msg[i] = $wordList[msg[i].to_i]
          i += 1
        end
      end
      if words.length == 2
        word1 = words[0]
        word2 = words[1]
        indexOfWord1 = $wordList.index(word1)
        indexOfWord2 = $wordList.index(word2)
        path = File.expand_path('../../../data/test3LevelFile.txt', __FILE__)
        File.open(path).each do |line|        
            tempArray = line.split(" ")
            if tempArray[0] == indexOfWord1.to_s
              i = 1
              while i < tempArray.length do
                if tempArray[i] == ';'
                  i += 1
                  if tempArray[i] == indexOfWord2.to_s
                    while i < tempArray.length do
                      if tempArray[i] == ','
                        i += 1
                        msg << tempArray[i]
                      elsif tempArray[i] == ';'
                        break
                      end
                      i += 1
                    end
                    break
                  end
                end
                i += 1
              end
            end                          
        end
        i = 0
        while i < msg.length do
          msg[i] = $documentList[msg[i].to_i]
          i += 1
        end        
      end
      if words.length == 3
        word1 = words[0]
        word2 = words[1]
        word3 = words[3]
        indexOfWord1 = $wordList.index(word1)
        indexOfWord2 = $wordList.index(word2)
        path = File.expand_path('../../../data/test3LevelFile.txt', __FILE__)
      end
      render :json => msg
    end


end
