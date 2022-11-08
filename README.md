# FileManager-FileExplorer

Creating a directory explorer-manager work_flow
V = implmented, X = TODO

1. Scan Folder V
 
2. Take data V
 - Choose Data Structure: Tree V
 - Choose parameters: V
    - Name --> Not Unique (For Files and Folders)
    - FullPath --> Unique (For Files and Folders)
    - Type --> Not Unique (fileExtension for Files, "Folder" for Folders)
    - Size --> Not Unique (For Files) 
       - [sum al child files of a folder and print total size?] X
    - Child/Parent relationships --> Not Unique (Child if root, child & parent if subdir, parent if file)
    - 
3. Printing outputs V
  - Tree structure (output in terminal AND/OR .txt file) V
  - Dictionary (Json if web, .txt is log file) V
  - List (csv table for excel et al., with panda) V
  - 
4. Searching for objects of the tree  X
  - Search by name, type, size etc...  
  - Searching for file duplicates. Matching sizes, then hashes 
  - Implement output for queries
  - 
5. Move, Rename, Delete, Create new, Open, Copy   X

6. Implement GUI? Web App? X
  
