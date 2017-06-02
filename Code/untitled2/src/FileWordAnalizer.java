import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * Created by judit on 15.05.17.
 */
public class FileWordAnalizer {

    private FilePartReader filePartReader;

    public FileWordAnalizer(FilePartReader filePartReader) {
        this.filePartReader = filePartReader;
    }

    public FilePartReader getFilePartReader() {
        return filePartReader;
    }

    public void setFilePartReader(FilePartReader filePartReader) {
        this.filePartReader = filePartReader;
    }

    public ArrayList<String> wordsByABC() throws IOException {
        ArrayList<String> words = new ArrayList<String>(Arrays.asList(filePartReader.readLines().split(" ")));
        Collections.sort(words);
        return words;
    }

    public ArrayList wordsContainingSubString(String subString) throws IOException {
        ArrayList<String> words = new ArrayList<String>(wordsByABC());
        ArrayList<String> wordsContainingSubstring = new ArrayList<>();

        for (String word : words) {
            if (word.contains(subString)) {
                wordsContainingSubstring.add(word);
            }
        }

        return wordsContainingSubstring;
    }

    public ArrayList wordsArePalindrome() throws IOException {
        ArrayList<String> words = new ArrayList<String>(wordsByABC());
        ArrayList<String> palindromeWords = new ArrayList<String>();

        for (String word : words) {
            StringBuffer buffer = new StringBuffer(word);
            buffer.reverse();
            if (word.contentEquals(buffer)) {
                palindromeWords.add(word);
            }
        }

        return palindromeWords;
    }

}
