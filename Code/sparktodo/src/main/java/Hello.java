/**
 * Created by judit on 09.05.17.
 */

import static spark.Spark.*;

public class Hello {
    public static void main(String[] args) {
        get("/hello", (req, res) -> "Hello World");
    }
}
