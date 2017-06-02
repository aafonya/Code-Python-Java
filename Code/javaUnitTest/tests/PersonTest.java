import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Created by judit on 10.05.17.
 */
class PersonTest {
    @Test
    public void TestIsNameIsNotNull() {
        Person John = new Person("John", 30);
        assertNotNull(John.getName());
    }

    @Test
    public void testIsAgeBelow0ThrowsException() {
        Person John = new Person("John", 30);
        assertThrows(IllegalArgumentException.class, () -> {
            John.setAge(-10);
        });
    }

}