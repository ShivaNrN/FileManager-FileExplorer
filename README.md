# FileManager-FileExplorer
Creating a directory explorer-manager work_flow
V = implmented, X = TODO

1. Scan Folder                                                                    V
2. Take data 
  2.1. Choose Data Structure: Tree                                                V
  2.2. Choose parameters:                                                         V
    2.2.1. Name --> Not Unique (For Files and Folders)
    2.2.2. FullPath --> Unique (For Files and Folders)
    2.2.3. Type --> Not Unique (fileExtension for Files, "Folder" for Folders)
    2.2.4. Size --> Not Unique (For Files) 
           [sum al child files of a folder and print total size?]                 X
    2.2.5. Child/Parent relationships --> Not Unique (Child if root, child & parent if subdir, parent if file)
3. Printing outputs                                                               V
    3.1. Tree structure (output in terminal AND/OR .txt file)                     V
    3.2. Dictionary (Json if web, .txt is log file)                               V
    3.3. List (csv table for excel et al., with panda)                            V
4. Searching for objects of the tree                                              X
    4.1. Search by name, type, size etc...  
    4.2. Searching for file duplicates. Matching sizes, then hashes 
    4.3. Implement output for queries
5. Move, Rename, Delete, Create new, Open, Copy                                   X
6. Implement GUI? Web App?                                                        X
  
