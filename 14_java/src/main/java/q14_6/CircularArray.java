package q14_6;

import java.util.Iterator;

public class CircularArray<T> implements Iterable<T> {
    private final T[] items;
    private int head = 0;

    @SuppressWarnings("unchecked")
    public CircularArray(int size) {
        items = (T[]) new Object[size];
    }

    private int convert(int index) {
        if (index < 0) {
            index += items.length;
        }
        return (head + index) % items.length;
    }

    public void rotate(int shiftRight) {
        head = convert(shiftRight);
    }

    public T get(int i) {
        if (i < 0 || i >= items.length) {
            throw new java.lang.IndexOutOfBoundsException();
        }
        return items[convert(i)];
    }

    public void set(int i, T item) {
        items[convert(i)] = item;
    }

    @Override
    public Iterator<T> iterator() {
        return new CircularArrayIterator<>(this);
    }

    private class CircularArrayIterator<TI> implements Iterator<TI> {
        // current = circular array の head の位置
        private int _current = -1;
        private final TI[] _items;

        public CircularArrayIterator(CircularArray<TI> array) {
            _items = array.items;
        }

        @Override
        public boolean hasNext() {
            return _current < (items.length - 1);
        }

        @Override
        public TI next() {
            _current++;
            return _items[convert(_current)];
        }

    }
}
