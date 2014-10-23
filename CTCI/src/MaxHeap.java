import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

/**
 * Created by aihe on 10/22/14.
 */
public class MaxHeap<T extends Comparable<T>> {

    private List<T> list;
    private int len;
    private List<T> unmodifiedList;

    public MaxHeap(){
        list = new ArrayList<T>();
        len = list.size();
    }

    public MaxHeap(Collection<? extends T> collection){
        list = new ArrayList<T>(collection);
        len = list.size();
        for (int i = len >> 1; i >= 0 ; --i){
            heapify(i);
        }
    }

    public void insert(T t){
        list.add(t);
        len += 1;
        int i = len - 1;
        while (i != 0){
            int parent = (i - 1) >>> 1;
            if (list.get(i).compareTo(list.get(parent)) > 0){
                Collections.swap(list, i, parent);
                i = parent;
            }
        }
    }

    public T pop(){
        T res = list.get(0);
        Collections.swap(list, 0, len - 1);
        len -= 1;
        heapify(0);
        return res;
    }

    private void heapify(int i ){
        int largeIdx = i;
        int left = (i << 1) + 1, right = (1 << 1) + 2;
        if (left < len){
            if (list.get(left).compareTo(list.get(largeIdx)) > 0){
                largeIdx = left;
            }
        }
        if (right < len){
            if (list.get(right).compareTo(list.get(largeIdx)) > 0){
                largeIdx = right;
            }
        }
        if (largeIdx != i){
            Collections.swap(list, largeIdx, i);
            heapify(i);
        }
    }

    public List<T> showList(){
        return unmodifiedList == null ? Collections.unmodifiableList(list) : unmodifiedList;
    }

    public static void main(String [] args){
        int M = 1000000;
        long start = System.currentTimeMillis();
        MaxHeap<Integer> maxHeap = new MaxHeap<Integer>();
        for(int i = 0; i < M; ++i){
            maxHeap.insert(i);
        }
        System.out.println(System.currentTimeMillis() - start);
//        List<Integer> showList = maxHeap.showList();
//        System.out.println(showList);
//        maxHeap.insert(10);
//        System.out.println(showList);

        long start1 = System.currentTimeMillis();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < M; ++i){
            list.add(i);
        }
        MaxHeap<Integer> maxHeap1 = new MaxHeap<Integer>(list);
        System.out.println(System.currentTimeMillis() - start1);
//        System.out.println(maxHeap1.showList());
    }
}
