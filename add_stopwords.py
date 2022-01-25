import csv

STOPWORDS_FILE = "stopwords.txt"
STOPWORDS_NEW_FILE = "data/new_stopwords.txt"

if __name__ == "__main__":
    # Stopwords new list that gonna be added
    sw_new_box = dict()
    with open(STOPWORDS_NEW_FILE, "r") as sw_new_file:
        sw_new_box = sw_new_file.read().split("\n")
    
    # Stopwords from git
    with open(STOPWORDS_FILE, "r+") as sw_file:
        sw_box = sw_file.read().split("\n")
        
        # Combine all sw  
        final_box = sw_box + sw_new_box
        
        clean_box = list(set(final_box))
        clean_box.sort()
    
        for row in clean_box:
            sw_file.write(row)
            sw_file.write("\n")
            
    # Reset new_stopwords.txt as blank file
    with open(STOPWORDS_NEW_FILE, 'w') as f:
        pass
     
    