class AnalysesController < ApplicationController


    def index
      $wordList = Array.new
      path = File.expand_path('../../../python/LindemannsPython3/LindemannsPython3/WordListFile.txt', __FILE__)
      File.open(path).each do |line|
          $wordList.append(line)
      end
      $wordList = $wordList.map {|x| x.chomp}

      $documentNameList = Array.new
      path = File.expand_path('../../../python/LindemannsPython3/LindemannsPython3/textHeaders.txt', __FILE__)
      file = File.open(path, "rb")
      $documentNameList = file.read
      $documentNameList = $documentNameList.split("\\**\\")
      $documentNameList = $documentNameList.map {|x| x.strip}
      $documentNameList = $documentNameList.reject { |x| x.empty? }

      $documentList = Array.new
      path = File.expand_path('../../../python/LindemannsPython3/LindemannsPython3/textDocuments.txt', __FILE__)
      file = File.open(path, "rb")
      $documentList = file.read
      $documentList = $documentList.split("\\**\\")
      $documentList = $documentList.map {|x| x.strip}
      $documentList = $documentList.reject { |x| x.empty? }
      puts ($wordList[37])
      @analyses = $wordList
    end

    def show
      word = ''
      params.each do |key, value|
        word = value
      end
      words = word.split("+")

      if words.length == 1
        msg = Array.new            
        indexOfWord1 = $wordList.index(word)
        path = File.expand_path('../../../python/LindemannsPython3/LindemannsPython3/test3LevelFile.txt', __FILE__)
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
        msg = Hash.new
        arrayOfIndexes = Array.new
        word1 = words[0]
        word2 = words[1]
        indexOfWord1 = $wordList.index(word1)
        indexOfWord2 = $wordList.index(word2)

        path = File.expand_path('../../../python/LindemannsPython3/LindemannsPython3/test3LevelFile.txt', __FILE__)
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
                        arrayOfIndexes << tempArray[i]
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
        arrayOfDocumentNames = Array.new
        while i < arrayOfIndexes.length do             
          arrayOfDocumentNames[i] = $documentNameList[arrayOfIndexes[i].to_i]     
          i += 1
        end        
        msg['names'] = arrayOfDocumentNames
        msg['indexes'] = arrayOfIndexes

      end
      if words.length == 3
        msg = Array.new
        word1 = words[0]
        word2 = words[1]
        word3 = words[2]

        msg[0] = $documentList[word3.to_i]
      end
      render :json => msg
    end


end
