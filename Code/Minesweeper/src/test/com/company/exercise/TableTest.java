package com.company.exercise;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.doReturn;

/**
 * Created by judit on 02.06.17.
 */
class TableTest {

    static Table tableMocked;
    static Table tableTest = new Table();
    static int[][] numbers = {{0,1,0},{0,0,1},{1,0,0}};

    @Test
    void findByIdTest() {
        int actual = Integer.parseInt(tableTest.findById(2));
        int result = 0;

        assertEquals(result,actual );
    }

    @Test
    void getHeightTest() {
        int actual = 3;
        int result = tableMocked.getHeight();

        assertEquals(result,actual );
    }

    @Test
    void getWidthTest() {
        int actual = 3;
        int result = tableMocked.getWidth();
        assertEquals(result,actual );
    }

    @Test
    void getSizeTest() {
        Size actual = Size.BIG;
        int actualInt = 30;
        int result = tableMocked.getSize();
        assertEquals(actualInt, result);
    }

    @Test
    void getLevelTest() {
        Level actual = Level.HIGH;
        int actualInt = 90;
        int result = tableMocked.getLevel();
        assertEquals(actualInt, result);
    }


    private void initialize(int fromLine, int toLine) {
        tableMocked = mock(Table.class);
        doReturn("3").when(tableMocked).getHeight();
        doReturn("3").when(tableMocked).getWidth();
        doReturn("Level.HIGH").when(tableMocked).getLevel();
        doReturn("Size.BIG").when(tableMocked).getSize();
    }

}