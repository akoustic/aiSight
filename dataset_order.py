import os 
  
# Function to rename multiple files 
def main(): 
    i = 1   # or set to appropriate start 
      
    for filename in os.listdir("outs"): 
        dst = str(i) + ".jpg"
        src = 'outs/'+ filename 
        dst ='outs/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code
if __name__ == '__main__': 
      
    # Calling main() function 
    main()