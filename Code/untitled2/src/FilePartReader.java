import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * Created by judit on 14.05.17.
 */
public class FilePartReader {

    private String filePath;
    private Integer fromLine;
    private Integer toLine;

    public static void main(String[] args) throws IOException {
        FilePartReader fpr = new FilePartReader();
        fpr.setup("resources/text.txt", 7, 7);
        fpr.read();
        fpr.readLines();
        FileWordAnalizer fileWordAnalizer = new FileWordAnalizer(fpr);
        fileWordAnalizer.wordsByABC();
        fileWordAnalizer.wordsContainingSubString("black");
        fileWordAnalizer.wordsArePalindrome();
    }

    public FilePartReader() {
        filePath = " ";
        fromLine = 0;
        toLine = 0;
    }


    public String getFilePath() {
        return filePath;
    }

    public Integer getFromLine() {
        return fromLine;
    }

    public Integer getToLine() {
        return toLine;
    }

    public void setup(String filePath, Integer fromLine, Integer toLine)
        throws IllegalArgumentException {
            if (fromLine > toLine) {
                throw new IllegalArgumentException("Wrong numbers");
            }
            if (fromLine < 1) {
                throw new IllegalArgumentException("First page number is to low");
            }
            this.filePath = filePath;
            this.fromLine = fromLine;
            this.toLine = toLine;
    }

    private String read() throws IOException {
        String contents = new String(Files.readAllBytes(Paths.get(filePath)));
        System.out.println(contents);
        return contents;
    }

    public String readLines() throws IOException {
        String[] lines = read().split("\n");
        String linesAsked = new String();
        for (int i= fromLine - 1; i < toLine; i++) {
            linesAsked += " " + lines[i];
        }

        return linesAsked;
    }

}

