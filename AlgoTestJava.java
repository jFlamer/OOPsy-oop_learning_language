
public class Main {
    public static void main(String[] args) {
        var l = new java.util.ArrayList<>(java.util.Arrays.asList(10, 20, 30));
        java.util.HashMap<Object, Object> __map_3 = new java.util.HashMap<>();
        __map_3.put("a", 1);
        var d = __map_3;
        System.out.println(l.get(1));
        System.out.println(d.get("a"));
        var x = l.get(0);
        System.out.println(x);
        return;
    }
}