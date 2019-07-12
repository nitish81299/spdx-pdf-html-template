"""
This is small script/basic script for language conversion.

How to use:

1. Change the filenames which to be converted in the main function in inputFile and 
   outputFile and place them in the same directory with the script for easy use.
2. Change the dest value according to the preferred language.
3. And for "main" in the end of the script, do same as step 1 in the main function.
4. Now run the script with python.
5. A new file is created with the name you suggested.
6. Then, run the file with pandoc for its format conversion in PDf or HTMl using 

   pandoc input.md -o output.pdf --from markdown --template spdx-pdf-template --table-of-contents --listings --pdf-engine=xelatex

"""
import googletrans
def main(inputFile="input.md", outputFile="output.md"):

    file1 = open(inputFile, "r", encoding="utf8")

    file2 = open(outputFile, "w")

   
    translator = googletrans.Translator()

    TransOption = googletrans.LANGCODES
    

    article = file1.readlines()

  
    for sentence in article:
        file2.write(translator.translate(sentence, dest='la').text + "\n")

    file1.close()
    file2.close()


if __name__ == "__main__":
    main("input.md", "output.md")
