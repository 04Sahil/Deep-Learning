import java.util.LinkedList;

import javax.swing.text.html.HTMLDocument.Iterator;
public class dsa {
    public static void main(String[] args){
      try{  LinkedList<String> list = new LinkedList<String>();
        list.add("one");
        list.add("2");
        list.add("3");
        System.out.println(list);
        list.set(1,"4");
        // System.out.println(list);
        
            list.addFirst("6");
            for (String h : list){
                System.out.println(h);
            }
           System.out.println(list.removeFirst());
           System.out.println(list.get(0));
        //  LinkedList  sec_list =  (LinkedList) list.clone();
        // //  sec_list = list.clone();
        // System.out.println(sec_list);
        // System.out.println(list.contains(4));
        Iterator x = list.descendingIterator();
        while (x.hasNext()){
            System.out.println(x.next());
        }
    }
    catch (NullPointerException e) { 
        System.out.println("Exception thrown : " + e); 
    } 
    }

   
}
