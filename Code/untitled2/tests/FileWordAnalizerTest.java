import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Created by judit on 17.05.17.
 */
class FileWordAnalizerTest {
    @Test
    public void IsAlphabeticallySorted() throws IOException {
        FilePartReader fpr = new FilePartReader();
        fpr.setup("resources/test.txt", 1, 4);
        FileWordAnalizer fileWordAnalizer = new FileWordAnalizer(fpr);
        String firstWord = fileWordAnalizer.wordsByABC().get(0);
        String lastWord = fileWordAnalizer.wordsByABC().get(7);

        String firstTestWord = "aa";
        String lastTestWord = "zz";

        assertEquals(firstTestWord, firstWord);
        assertEquals(lastTestWord, lastWord);

    }

    @Test
    public void WordsContainingSubstring() throws IOException {
        FilePartReader fpr = new FilePartReader();
        fpr.setup("resources/test.txt", 1, 4);
        FileWordAnalizer fileWordAnalizer = new FileWordAnalizer(fpr);

        String subString5x = "aa";
        String subString1x = "gvds";

        int countSubStr5x = fileWordAnalizer.wordsContainingSubString(subString5x).size();
        int countSubStr1x = fileWordAnalizer.wordsContainingSubString(subString1x).size();

        assertEquals(5, countSubStr5x);
        assertEquals(1, countSubStr1x);
    }

    @Test
    public void testAllWordsArePalindrome() throws IOException {
        FilePartReader fpr = new FilePartReader();
        fpr.setup("resources/text.txt", 7, 7);
        FileWordAnalizer fileWordAnalizer = new FileWordAnalizer(fpr);

        String firstPalindrome = "aa";
        String lastPalindrome = "zz";
        String notPalindrome = "ddaadc";

        assertTrue(fileWordAnalizer.wordsArePalindrome().get(0).equals(firstPalindrome));
        assertTrue(fileWordAnalizer.wordsArePalindrome().get(4).equals(firstPalindrome));
        assertFalse(fileWordAnalizer.wordsArePalindrome().contains(notPalindrome));
    }

}