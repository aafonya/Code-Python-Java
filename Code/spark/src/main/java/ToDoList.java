/**
 * Created by judit on 09.05.17.
 */
import java.util.ArrayList;

public class ToDoList {

    private int id;
    private String title;
    private int priority;

    private static int idCount = 0;

    private static ArrayList<ToDoList> toDoList;

    public ToDoList(String title, int priority) {
        this.title = title;
        this.priority = priority;

        id = idCount++;
        toDoList.add(this);
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public static ArrayList<ToDoList> getToDoList() {
        return toDoList;
    }

    public static void setToDoList(ArrayList<ToDoList> toDoList) {
        ToDoList.toDoList = toDoList;
    }

    @Override
    public String toString() {
        return "ToDoList{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", priority=" + priority +
                '}';
    }
}
