def main():
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        
        fruit_list.reverse()
        print(f'Reversed: {fruit_list}')
        
        fruit_list.append('orange')
        print(f'append orange: {fruit_list}')
        
        find_apple = 'apple'
        insert_cherry = 'cherry'
        index = fruit_list.index(find_apple)
        fruit_list.insert(index, insert_cherry)
        print(f'insert orange: {fruit_list}')
        
        fruit_list.remove('banana')
        print(f'remove banana: {fruit_list}')
        
        popped_element = fruit_list[-1]
        fruit_list.pop()
        print(f'pop orange: {fruit_list}')
        
        fruit_list.sort()
        print(f'sorted: {fruit_list}')
        
        fruit_list.clear()
        print(f'cleared: {fruit_list}')
        
        
        
        
        
        
if __name__ == "__main__":
    main()