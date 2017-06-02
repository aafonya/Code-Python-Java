import spark.ModelAndView;
import spark.Request;
import spark.Response;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by judit on 09.05.17.
 */
public class ToDoListController {
    public static ModelAndView renderToDoList(Request req, Response res) {
        ToDoList newList = new ToDoList("new", 10);
        return new ModelAndView(newList, "product/welcome");
    }

    public static ModelAndView renderToDoList2(Request req, Response res) {

        Map params = new HashMap<>();
        ToDoList list = new ToDoList("New Title", 10);

        params.put("title", list.getTitle());
        params.put("priority", list.getPriority());
        return new ModelAndView(params, "product/welcome");
    }
}
